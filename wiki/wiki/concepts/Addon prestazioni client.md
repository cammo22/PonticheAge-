---
tags: [client, prestazioni, cryengine]
type: concept
aliases: [Addon prestazioni, Scatti, Stutter]
---
# Addon prestazioni del client

Obiettivo: eliminare gli scatti tipici di ArcheAge ([[CryEngine 3]]).

## Prima si misura
Niente correzioni alla cieca: si registrano i tempi di ogni fotogramma (PresentMon) in percorsi fissi (Solzreed a piedi, a cavallo, in volo, in mare, in citta' affollata) e si confrontano prima/dopo ogni modifica.

## Cause tipiche e rimedi da provare
| Causa | Rimedio |
|---|---|
| Compilazione degli shader durante il gioco | Traduzione D3D9/D3D10 -> Vulkan con cache e compilazione asincrona; precompilazione al primo avvio |
| Caricamento di modelli e texture sul thread principale | Variabili del motore per lo streaming + hook delle funzioni di caricamento in `cry3dengine.dll` |
| Allocatore di memoria lento/frammentato | Sostituire l'allocatore (il client usa gia' `tbbmalloc`/`shallocator.dll`) |
| Ritmo dei fotogrammi irregolare | Limitatore di fotogrammi preciso, timer ad alta risoluzione |
| Troppi personaggi in citta' | Livelli di dettaglio e distanze piu' aggressivi solo in quei casi |

## Come si aggancia
Una DLL nostra caricata dal launcher all'avvio del client. Le DLL di rendering (`cryrenderd3d10.dll`, `cryrenderd3d9.dll`) **non sono protette** da [[Themida]]: si analizzano subito con [[Ghidra]].
