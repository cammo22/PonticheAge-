"""Avvia il client e copia dalla memoria i moduli protetti da Themida, ricostruendo PE leggibili da Ghidra.

Registra anche cosa fa il client nei primi secondi: moduli caricati, finestre create, processi figli.

Uso:  python tools/dumper/dump_modules.py --client _local/client --out _local/re/dump [--seconds 40]
"""
import argparse, ctypes, ctypes.wintypes as wt, json, os, struct, subprocess, sys, time

k32 = ctypes.WinDLL("kernel32", use_last_error=True)
u32 = ctypes.WinDLL("user32", use_last_error=True)
psapi = ctypes.WinDLL("psapi", use_last_error=True)

PROCESS_QUERY_INFORMATION, PROCESS_VM_READ = 0x0400, 0x0010
TH32CS_SNAPMODULE, TH32CS_SNAPMODULE32, TH32CS_SNAPPROCESS = 0x8, 0x10, 0x2
MEM_COMMIT = 0x1000
PAGE_NOACCESS, PAGE_GUARD = 0x01, 0x100

TARGETS = {"x2game.dll", "crynetwork.dll", "crysystem.dll", "cry3dengine.dll", "cryphysics.dll", "archeage.exe"}


class MODULEENTRY32W(ctypes.Structure):
    _fields_ = [("dwSize", wt.DWORD), ("th32ModuleID", wt.DWORD), ("th32ProcessID", wt.DWORD),
                ("GlblcntUsage", wt.DWORD), ("ProccntUsage", wt.DWORD), ("modBaseAddr", ctypes.c_void_p),
                ("modBaseSize", wt.DWORD), ("hModule", wt.HMODULE), ("szModule", wt.WCHAR * 256),
                ("szExePath", wt.WCHAR * 260)]


class PROCESSENTRY32W(ctypes.Structure):
    _fields_ = [("dwSize", wt.DWORD), ("cntUsage", wt.DWORD), ("th32ProcessID", wt.DWORD),
                ("th32DefaultHeapID", ctypes.c_void_p), ("th32ModuleID", wt.DWORD), ("cntThreads", wt.DWORD),
                ("th32ParentProcessID", wt.DWORD), ("pcPriClassBase", wt.LONG), ("dwFlags", wt.DWORD),
                ("szExeFile", wt.WCHAR * 260)]


class MBI(ctypes.Structure):
    _fields_ = [("BaseAddress", ctypes.c_void_p), ("AllocationBase", ctypes.c_void_p), ("AllocationProtect", wt.DWORD),
                ("PartitionId", wt.WORD), ("RegionSize", ctypes.c_size_t), ("State", wt.DWORD),
                ("Protect", wt.DWORD), ("Type", wt.DWORD)]


k32.CreateToolhelp32Snapshot.restype = wt.HANDLE
k32.OpenProcess.restype = wt.HANDLE
k32.VirtualQueryEx.argtypes = [wt.HANDLE, ctypes.c_void_p, ctypes.POINTER(MBI), ctypes.c_size_t]
k32.ReadProcessMemory.argtypes = [wt.HANDLE, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)]


def modules(pid):
    snap = k32.CreateToolhelp32Snapshot(TH32CS_SNAPMODULE | TH32CS_SNAPMODULE32, pid)
    if snap in (None, wt.HANDLE(-1).value):
        return {}
    out, me = {}, MODULEENTRY32W()
    me.dwSize = ctypes.sizeof(me)
    ok = k32.Module32FirstW(snap, ctypes.byref(me))
    while ok:
        out[me.szModule.lower()] = (me.modBaseAddr, me.modBaseSize, me.szExePath)
        ok = k32.Module32NextW(snap, ctypes.byref(me))
    k32.CloseHandle(snap)
    return out


def processes():
    snap = k32.CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)
    out, pe = [], PROCESSENTRY32W()
    pe.dwSize = ctypes.sizeof(pe)
    ok = k32.Process32FirstW(snap, ctypes.byref(pe))
    while ok:
        out.append((pe.th32ProcessID, pe.th32ParentProcessID, pe.szExeFile))
        ok = k32.Process32NextW(snap, ctypes.byref(pe))
    k32.CloseHandle(snap)
    return out


def windows(pids):
    found = []
    WNDENUMPROC = ctypes.WINFUNCTYPE(wt.BOOL, wt.HWND, wt.LPARAM)

    def cb(hwnd, _):
        pid = wt.DWORD()
        u32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
        if pid.value in pids:
            t, c = ctypes.create_unicode_buffer(256), ctypes.create_unicode_buffer(256)
            u32.GetWindowTextW(hwnd, t, 256)
            u32.GetClassNameW(hwnd, c, 256)
            found.append((pid.value, c.value, t.value, bool(u32.IsWindowVisible(hwnd))))
        return True
    u32.EnumWindows(WNDENUMPROC(cb), 0)
    return found


def read_image(h, base, size):
    """Legge l'immagine pagina per pagina; le parti illeggibili restano a zero."""
    buf = bytearray(size)
    addr, end = base, base + size
    while addr < end:
        mbi = MBI()
        if not k32.VirtualQueryEx(h, addr, ctypes.byref(mbi), ctypes.sizeof(mbi)):
            break
        region_end = min(mbi.BaseAddress + mbi.RegionSize, end)
        n = region_end - addr
        if mbi.State == MEM_COMMIT and not (mbi.Protect & (PAGE_NOACCESS | PAGE_GUARD)):
            tmp = (ctypes.c_char * n)()
            got = ctypes.c_size_t()
            if k32.ReadProcessMemory(h, addr, tmp, n, ctypes.byref(got)):
                buf[addr - base:addr - base + got.value] = tmp.raw[:got.value]
        addr = region_end
    return buf


def fix_pe(img, base):
    """Allinea le sezioni su disco a quelle in memoria e imposta l'ImageBase reale."""
    e = struct.unpack_from("<I", img, 0x3C)[0]
    if img[e:e + 4] != b"PE\0\0":
        return img
    nsec = struct.unpack_from("<H", img, e + 6)[0]
    optsz = struct.unpack_from("<H", img, e + 20)[0]
    opt = e + 24
    magic = struct.unpack_from("<H", img, opt)[0]
    if magic == 0x20B:
        struct.pack_into("<Q", img, opt + 24, base)
    else:
        struct.pack_into("<I", img, opt + 28, base)
    sect_align = struct.unpack_from("<I", img, opt + 32)[0]
    struct.pack_into("<I", img, opt + 36, sect_align)  # FileAlignment = SectionAlignment
    for i in range(nsec):
        s = opt + optsz + 40 * i
        vsize, va = struct.unpack_from("<II", img, s + 8)
        struct.pack_into("<II", img, s + 16, vsize, va)  # SizeOfRawData, PointerToRawData
    return img


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--client", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--seconds", type=int, default=40)
    ap.add_argument("--args", default="-StrUserName ponte -strUserToken test -serverId 1 -sIp 127.0.0.1 -sPort 1237 -gameId 1")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    exe = os.path.abspath(os.path.join(a.client, "bin64", "archeage.exe"))
    before = {p[0] for p in processes()}
    proc = subprocess.Popen([exe] + a.args.split(), cwd=os.path.dirname(exe))
    t0, log, seen_mods, seen_wnd, seen_proc, dumped = time.time(), [], set(), set(), set(), {}
    family = {proc.pid}

    def note(kind, data):
        log.append({"t": round(time.time() - t0, 2), "kind": kind, **data})
        print(f"[{log[-1]['t']:6.2f}] {kind} {data}", flush=True)

    note("start", {"pid": proc.pid, "exe": exe})
    while time.time() - t0 < a.seconds:
        for pid, ppid, name in processes():
            if pid not in before and (ppid in family or pid in family) and pid not in seen_proc:
                family.add(pid); seen_proc.add(pid); note("process", {"pid": pid, "parent": ppid, "name": name})
        for pid in list(family):
            for name, (base, size, path) in modules(pid).items():
                if (pid, name) not in seen_mods:
                    seen_mods.add((pid, name)); note("module", {"pid": pid, "name": name, "base": hex(base), "size": size})
        for w in windows(family):
            if w not in seen_wnd:
                seen_wnd.add(w); note("window", {"pid": w[0], "class": w[1], "title": w[2], "visible": w[3]})
        # Copia ripetuta: l'ultima e' la piu' completa (codice gia' decifrato)
        for pid in list(family):
            mods = modules(pid)
            for name in TARGETS & mods.keys():
                base, size, _ = mods[name]
                h = k32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, pid)
                if not h:
                    continue
                img = read_image(h, base, size)
                k32.CloseHandle(h)
                if sum(1 for b in img[:0x1000] if b) > 0:
                    with open(os.path.join(a.out, name), "wb") as f:
                        f.write(fix_pe(img, base))
                    dumped[name] = {"base": hex(base), "size": size, "t": round(time.time() - t0, 2)}
        if proc.poll() is not None and not any(p[0] in family for p in processes() if p[0] != proc.pid):
            note("exit", {"code": proc.returncode}); break
        time.sleep(1)
    # chiude solo i processi avviati da questo script
    for pid in family:
        subprocess.run(["taskkill", "/PID", str(pid), "/T", "/F"], capture_output=True)
    json.dump({"log": log, "dumped": dumped}, open(os.path.join(a.out, "timeline.json"), "w"), indent=1)
    print("copiati:", json.dumps(dumped, indent=1))


if __name__ == "__main__":
    main()
