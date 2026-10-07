---
tags: [protezione, reverse-engineering]
type: entity
aliases: [WinLicense, Oreans]
---
# Themida

Protezione commerciale (Oreans) che cifra il codice sul disco e lo decifra in memoria all'avvio. Riconoscibile dalle sezioni con nomi casuali (`fgwbjhsg`, `vtrtqznr`...), da una prima sezione vuota su disco ma enorme in memoria (68 MB per `x2game.dll`) e dalla sezione `.taggant`.

Nel [[Client AA 9.0.2.9]] protegge `archeage.exe`, `x2game.dll`, `crynetwork.dll`, `crysystem.dll`, `cry3dengine.dll`, `cryphysics.dll`. Non protetti: `cryrenderd3d9/10.dll`, `cryaction`, `cryanimation`, `cryentitysystem`, `cryscriptsystem`, `xlcommon`.

## Come si aggira per l'analisi
Si avvia il client, si aspetta che sia in schermata di login (codice ormai decifrato), e un programma nostro copia i moduli dalla memoria ricostruendo un PE con le sezioni allineate. [[Ghidra]] analizza poi il file copiato. Le importazioni possono risultare offuscate: si ricostruiscono dagli indirizzi delle DLL di sistema.
