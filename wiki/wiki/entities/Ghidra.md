---
tags: [strumento, reverse-engineering]
type: entity
aliases: []
---
# Ghidra

Disassemblatore/decompilatore della NSA. Versione 12.1.4 + JDK 21 portatile in `_local/tools`.

```bash
# analisi completa (lenta)
tools/ghidra/ghidra.sh 'C:\Users\cammo\Desktop\PONTIC~1.0\_local\re\ghidra-proj' AA9 -import <file> -overwrite \
  -scriptPath 'C:\Users\cammo\Desktop\PONTIC~1.0\tools\ghidra' -postScript DumpStrings.java <out.tsv>
# domande su un file gia' analizzato (~1 minuto)
tools/ghidra/ghidra.sh <progetto> AA9 -process <file> -noanalysis -scriptPath <scripts> -postScript Decomp.java <out> <stringa>
```
Il percorso del progetto ha uno spazio: si usa sempre il nome corto `PONTIC~1.0`.

| Script (`tools/ghidra`) | Cosa fa |
|---|---|
| `DumpStrings.java` | tutte le stringhe con le funzioni che le usano |
| `Decomp.java` | decompila le funzioni che usano una stringa |
| `LuaBind.java` | dalla stringa di una funzione Lua/cvar al codice che la registra |
| `DecompAt.java` | decompila a un indirizzo, con i chiamati |
