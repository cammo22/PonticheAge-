---
tags: [piano, stima, decisione]
type: concept
aliases: [Stima, Fattibilita, Quanto ci vuole]
---
# Fattibilita' e stima dei tempi

## Si puo' scrivere il server da zero?
**Si', e' fattibile**, ma e' il lavoro piu' grande del progetto. Il client contiene molto: tutte le tabelle del gioco (oggetti, skill, buff, quest, ricette, gradi, pass, negozi), le mappe, il terreno, le animazioni, la logica di interfaccia in Lua. Quello che il client **non** contiene e che va ricostruito o inventato:

| Cosa manca nel client | Come lo otteniamo |
|---|---|
| Il protocollo di rete (codici dei pacchetti, cifratura) | Reverse engineering di `x2game.dll` e `crynetwork.dll` dopo averli estratti dalla memoria ([[Themida]]) |
| Posizioni di NPC e mostri | Da verificare: i livelli nel game_pak contengono gli "spawner" delle entita' (ipotesi forte). Altrimenti posizionamento nostro |
| Tabelle di loot, comportamento dei mostri (IA), formule di danno | Le progettiamo noi, partendo dai dati del client (che ha le formule di tooltip). E' anche l'occasione per rendere il gioco "diverso", come vuoi |
| Logica di eventi e assedi | Ricostruita dai dati + design nostro |

Partire da zero ha un vantaggio vero: un'architettura sola e pulita (un processo, niente "zone host" esterni, niente patch sopra codice altrui), ed e' quello che ha rotto il vecchio progetto (vedi [[Lezioni da DaProd]]).

## AAEmu o da zero?
[[AAEmu]] non ha un ramo 9.0: ha 8.0 (marzo 2022) e 10.0.2. I codici dei pacchetti cambiano a ogni versione, quindi per la 9.0.2.9 il reverse engineering del protocollo va fatto comunque. Scelta presa: **da zero, in [[Clean room]]**. Unica nota onesta: consultare AAEmu solo come *documentazione* della forma dei pacchetti (non il codice) farebbe risparmiare forse il 25-35% del tempo nelle fasi 1-2. Si decide caso per caso, solo con il tuo ok.

## "Nemmeno un bug"
Nessun software di queste dimensioni ha zero bug, e prometterlo sarebbe falso. Quello che posso promettere e misurare:
- ogni funzione entra **solo** con test automatici che la provano (client finto che parla il protocollo vero, vedi [[Qualita e test]]);
- **zero bug noti bloccanti** al rilascio della v1.0.0;
- ogni bug trovato diventa un test, cosi' non torna.

## Stima per la v1.0.0 completa
Ipotesi: io scrivo il codice in sessioni regolari (quasi tutti i giorni), tu provi in gioco con le istruzioni passo-passo. Il collo di bottiglia non e' scrivere codice: e' il reverse engineering e la verifica in gioco.

| Fase | Contenuto | Durata |
|---|---|---|
| 0. Fondamenta | Dump del client da memoria, Ghidra, formato game_pak, database del client, tabella dei pacchetti, client finto per i test, CI | 3-5 settimane |
| 1. Entrare nel mondo | Login, lista server, creazione personaggio, ingresso, movimento, chat, vedere gli altri giocatori, launcher nuovo | 1,5-3 mesi |
| 2. Gioco base | Combattimento, skill e buff, NPC e mostri con IA, loot, quest, inventario, livelli e livelli ancestrali, equipaggiamento con gradi e potenziamenti (Hiram fino a Celestial e oltre) | 4-6 mesi |
| 3. Vita ed economia | Raccolta, crafting, case e fattorie, trade pack, posta, asta, negozio, pass, daily, punti onore e vocazione spendibili | 3-4 mesi |
| 4. Mondo vivo | Cavalcature e mate, navi, gilde e famiglie, gruppi e raid, dungeon, PvP, arene, castelli e assedi | 3-5 mesi |
| 5. Rifinitura | [[Addon prestazioni client]], [[Pannello server]] nuovo, traduzione completa, beta con gli amici | 2-3 mesi |

**Totale realistico: 14-24 mesi**, stima centrale **circa 18 mesi** per una v1.0.0 con tutto il gioco.

Tappe intermedie giocabili (molto prima):
- **v0.1** (fine fase 1, ~3 mesi): si entra, si gira, si chatta.
- **v0.5** (fine fase 2, ~8 mesi): si livella e si combatte davvero.
- **v0.8** (fine fase 3, ~12 mesi): economia completa, si puo' giocare con gli amici.

Se si riduce la v1.0.0 a "PvE + vita ed economia" (assedi e navi nella 1.1) si scende a **9-12 mesi**.

## Addon DLSS 5
Fuori dalla stima della v1.0.0: e' un progetto di ricerca, vedi [[Upscaling e DLSS 5]].
