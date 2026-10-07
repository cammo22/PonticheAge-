---
tags: [strumento, reverse-engineering]
type: entity
aliases: [rea-agents]
---
# REA

"Reverse Engineer Anything" (morluto/rea, MIT): server MCP che collega l'agente a strumenti di reverse engineering (Hopper, [[Ghidra]], IDA). Copia in `_local/tools/rea`. Richiede Node.js 22+ (presente: 26).

## Valutazione (2026-10-07)
REA **non risolve** il nostro problema principale:
- Su Windows il collegamento a Ghidra e' sperimentale e accetta solo **eseguibili** x86-64, **non DLL**: `x2game.dll` e le altre sono DLL.
- Non toglie [[Themida]]: lavora sui file cosi' come sono, quindi vede lo stesso codice cifrato.
- La cattura del comportamento dei processi non funziona su Windows (solo Linux/macOS).

Dove puo' servire: con la versione Linux (WSL) per analizzare i moduli **dopo** averli estratti dalla memoria, e per confrontare due analisi. Per ora gli script headless di Ghidra in `tools/ghidra` fanno lo stesso lavoro.
