---
tags: [fonte, riferimento]
type: source
aliases: [Riferimenti, Client 10.0.2]
---
# Riferimenti dal client 10.0.2 (vecchio progetto)

Recuperati dal [[Progetto DaProdArcheage]] prima della pulizia, in `_local/ref` (non in git):

| Cartella | Contenuto | A cosa serve |
|---|---|---|
| `aa-10.0.2/bin64` | Moduli del client 10.0.2 **non protetti** (x2game, crynetwork, crysystem...) piu' i moduli `_dedicate` del motore lato server | Guida per il 9.0.2.9: il codice di versioni vicine e' molto simile. Le funzioni riconosciute nel 10.0.2 si ritrovano nel 9.0.2.9 dopo l'estrazione |
| `aa-10.0.2/compact_en.sqlite3` | Database del client 10.0.2 con testi inglesi (1003 tabelle) | Struttura delle tabelle, testi per la [[Localizzazione]] |
| `aa-10.0.2/*multilangual*.7z` | Database multilingua 10.0.2 | [[Localizzazione]] |
| `aa-10.0.2/game_decrypted.7z` | Database del gioco decifrato 10.0.2 | Confronto delle tabelle |
| `ghidra-10.0.2/` | Progetto Ghidra con x2game 10.0.2 gia' analizzato + elenchi di stringhe, funzioni Lua, variabili | Lettura veloce del codice 10.0.2 |
| `daprod-docs/` | Note e decompilati del vecchio progetto | Storico |

Sono file del gioco (XLGames), non codice [[AAEmu]]: usarli non viola la [[Clean room]].
