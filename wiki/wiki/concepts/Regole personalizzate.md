---
tags: [regole, design]
type: concept
aliases: [Regole, Regole di gioco, Modifiche al gioco]
---
# Regole personalizzate

Il gioco non sara' una copia dell'originale: le regole si piegano ai gusti del proprietario del server. Tecnicamente ogni regola e' un **dato** (file di configurazione), modificabile dal [[Pannello server]] anche a server acceso ([[Architettura server]], principio 4).

## Regole decise
| Regola | Originale | PonticheAge |
|---|---|---|
| **Serendipity Stone, scelta diretta** | Ogni pietra rimescola a caso un effetto di sintesi (costumi, mantelli, equipaggiamento Erenor) | Con **N pietre** (10-20, configurabile) si apre una finestra in gioco e si **sceglie direttamente** l'effetto di sintesi che si vuole. 1 pietra = rimescolamento casuale come prima |
| **Annulla effetto dell'arma, in gioco** | Nel vecchio progetto era il comando chat `/annulla` (non voluto) | Pulsante nell'interfaccia di gioco, sull'arma o sull'effetto, niente comandi chat |

## Come si realizza la scelta diretta
1. Il server conosce gia' la lista degli effetti possibili per ogni oggetto (tabelle di sintesi del database del client).
2. Serve una finestra nel client: l'interfaccia di ArcheAge e' in Lua dentro il game_pak, quindi si puo' aggiungere una finestra nostra (lista degli effetti + pulsante Conferma) e mandarla al client con il launcher.
3. Il server controlla tutto (pietre possedute, effetto ammesso): il client sceglie, il server decide.

## Da raccogliere
Scrivi qui (o dimmele) tutte le altre regole che vuoi cambiare: tassi di esperienza e loot, labor, costi di potenziamento, probabilita' di successo, limiti, eventi. Ogni regola diventa un'opzione del pannello con il suo test.
