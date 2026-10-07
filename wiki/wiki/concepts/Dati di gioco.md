---
tags: [dati, game_pak]
type: concept
aliases: [game_pak, Database del client]
---
# Dati di gioco

## game_pak
File unico da 49,6 GB in `_local/client/game_pak` (52.034.150.912 byte). Contiene i file del gioco (livelli, modelli, Lua dell'interfaccia, database). **Letto il 2026-10-07** con `tools/pak/pak_list.ps1`: intestazione `WIBO` in coda al file (AES-128-CBC, chiave pubblica nota del formato ArcheAge), 380.269 file + 494 extra, tabella dei file subito prima (voci da 0x150 byte, ognuna cifrata a se' con IV zero). I dati dei file sono **in chiaro**. Elenco completo in `_local/re/out/game_pak.files.tsv`. Il database del client e' `game/db/compact.sqlite` (59 MB). `game/version.txt` = `VERSION 9,0,2,9`.

## Database del client
Atteso in `game/db/` dentro il game_pak (sqlite, probabilmente cifrato). Contiene oggetti, skill, buff, quest, ricette, gradi di potenziamento, pass, negozi, testi localizzati. Il server lo converte al primo avvio in un formato suo, piu' veloce, e lo usa in sola lettura.

## Dati che il client non ha
- **Posizioni di NPC e mostri**: si cercano gli spawner nei file dei livelli (`game/worlds/...`). Se ci sono, sono la stessa fonte che usavano i server ufficiali.
- **Loot, IA, formule lato server**: progettati da noi, configurabili dal [[Pannello server]].

## Riferimenti locali (non in git)
- `_local/data/ref/aa-10.0.2.13r575-compact-multilangual-...7z`: database multilingua del client 10.0.2, utile come fonte di testi inglesi per la [[Localizzazione]] (gli id di molte righe coincidono tra versioni vicine).
