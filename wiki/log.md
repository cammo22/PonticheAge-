---
tags: [log]
type: log
---
# Diario

## 2026-10-07: ripartenza da zero
- Chiuso l'esperimento [[Progetto DaProdArcheage]] (server AAEmu 10.0.2): troppi sistemi rotti, vedi [[Lezioni da DaProd]].
- Nuova repo `cammo22/PonticheAge-`, cartella `Desktop\PontichAge 2.0`.
- Archivio del client analizzato: e' **solo client**, coreano KX, 52,8 GB (game_pak 49,6 GB). Vedi [[Archivio client 9.0.2.9]].
- `x2game.dll`, `crynetwork.dll`, `crysystem.dll`, `archeage.exe` sono protetti da [[Themida]]: Ghidra non li puo' leggere da disco. Primo compito tecnico: estrarli dalla memoria con un dumper nostro.
- `cryrenderd3d10.dll` e `cryrenderd3d9.dll` NON sono protetti: si possono analizzare subito per l'[[Addon prestazioni client]].
- Strumenti copiati in `_local/tools`: [[Ghidra]] 12.1.4 + JDK 21, 7-Zip, [[Universal Modder]], [[REA]].
- Vault Obsidian creato con il plugin Karpathy LLM Wiki 1.28.0.
- Scritte: [[Fattibilita e stima]], [[Roadmap v1.0.0]], [[Architettura server]], [[Rischi]].
- Pipeline Ghidra verificata su `cryrenderd3d10.dll` (non protetta): 10.940 stringhe, trovate le variabili degli shader asincroni ([[Addon prestazioni client]]). Nota tecnica in [[Ghidra]]: percorsi con `/` e nome corto 8.3.
- Correzione: anche `cry3dengine.dll` e `cryphysics.dll` sono protetti da [[Themida]] (Ghidra ne ha letto solo 34 stringhe). Elenco aggiornato in [[Client AA 9.0.2.9]].
