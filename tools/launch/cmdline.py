"""Costruisce la riga di comando del client 9.0.2.9 come fa il patcher XLGames (bin32/patcher.exe, FUN_00490670).

Primo argomento: 16 caratteri = 12 byte offuscati con l'indirizzo del server di login (i "commands" che
CrySystem legge all'avvio; se mancano: "Failed to load commands!"). Layout dei 12 byte, prima dell'XOR:
  0 porta & 0xFF     1 ip[0]   2 porta >> 8   3 ip[1]   4 ip[3]   5 ip[2]
  6 casuale          7 casuale 8 checksum     9 casuale 10 chiave  11 flag (byte di config del patcher a +0xb95)
checksum = somma (mod 256) di tutti i byte tranne l'8, & 0x3F; poi XOR con la chiave su tutti i byte tranne il 10.
Codifica: base64 di xlcommon.dll (encode_base64): alfabeto "./0-9A-Za-z", 3 byte -> 4 caratteri, little-endian.

Secondo pezzo (modalita'): "-k" | "-k <chiave>" | "-y -locale <lingua> -instant_token <token>" | "-j a|b|c|d|e|f|g h".
"""
import argparse, random, socket

ALPHABET = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def encode3(a, b, c):
    v = a | (b << 8) | (c << 16)
    return "".join(ALPHABET[(v >> s) & 0x3F] for s in (0, 6, 12, 18))


def decode4(s):
    v = sum(ALPHABET.index(ch) << (6 * i) for i, ch in enumerate(s))
    return [v & 0xFF, (v >> 8) & 0xFF, (v >> 16) & 0xFF]


def build_blob(ip, port, flag=0, rng=random):
    o = list(socket.inet_aton(ip))
    r = [rng.randint(1, 255) for _ in range(4)]
    b = [port & 0xFF, o[0], port >> 8, o[1], o[3], o[2], r[0], r[1], 0, r[2], r[3], flag & 0xFF]
    b[8] = sum(x for i, x in enumerate(b) if i != 8) & 0xFF & 0x3F
    key = b[10]
    b = [x if i == 10 else x ^ key for i, x in enumerate(b)]
    return "".join(encode3(*b[i:i + 3]) for i in range(0, 12, 3))


def parse_blob(blob):
    """Operazione inversa, per i test: restituisce (ip, porta, flag) e verifica il checksum."""
    b = sum((decode4(blob[i:i + 4]) for i in range(0, 16, 4)), [])
    key = b[10]
    b = [x if i == 10 else x ^ key for i, x in enumerate(b)]
    ok = (sum(x for i, x in enumerate(b) if i != 8) & 0x3F) == (b[8] & 0x3F)
    ip = "%d.%d.%d.%d" % (b[1], b[3], b[5], b[4])
    return ip, b[0] | (b[2] << 8), b[11], ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ip", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=1237)
    ap.add_argument("--flag", type=int, default=0)
    ap.add_argument("--mode", default="-k", help='es. "-k", "-y -locale en_us -instant_token abc"')
    a = ap.parse_args()
    blob = build_blob(a.ip, a.port, a.flag)
    assert parse_blob(blob)[:3] == (a.ip, a.port, a.flag) and parse_blob(blob)[3]
    print(f"{blob} {a.mode}")


if __name__ == "__main__":
    main()
