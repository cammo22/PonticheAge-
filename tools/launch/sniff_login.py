"""Mini server TCP che accetta il client sulla porta di login e registra in esadecimale cio' che riceve.
Non risponde nulla: serve solo a vedere il primo pacchetto del protocollo.
Uso: python tools/launch/sniff_login.py [--port 1237] [--out _local/re/out/login_first.bin] [--seconds 150]
"""
import argparse, socket, time


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=1237)
    ap.add_argument("--out", default="_local/re/out/login_first.bin")
    ap.add_argument("--seconds", type=int, default=150)
    a = ap.parse_args()
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", a.port))
    srv.listen(4)
    srv.settimeout(a.seconds)
    print(f"in ascolto su 127.0.0.1:{a.port}", flush=True)
    data = b""
    try:
        conn, addr = srv.accept()
        print("connesso:", addr, flush=True)
        conn.settimeout(15)
        t0 = time.time()
        while time.time() - t0 < 15:
            try:
                chunk = conn.recv(65536)
            except socket.timeout:
                break
            if not chunk:
                break
            data += chunk
            print(f"+{len(chunk)} byte (totale {len(data)})", flush=True)
        conn.close()
    except socket.timeout:
        print("nessuna connessione", flush=True)
    open(a.out, "wb").write(data)
    for i in range(0, len(data), 16):
        row = data[i:i + 16]
        print(f"{i:04x}  {row.hex(' '):<48}  {''.join(chr(c) if 32 <= c < 127 else '.' for c in row)}")


if __name__ == "__main__":
    main()
