---
tags: [client, launcher, requisito]
type: concept
aliases: [Piu client, Multi client, Altri ArcheAge]
---
# Client multipli e identita' separata

**Requisito:** aprire PonticheAge non deve chiudere gli altri ArcheAge del PC (altre installazioni, altri server). PonticheAge deve sembrare un programma diverso.

## Cosa sappiamo
- Il vecchio launcher DaProd **non** chiudeva processi del gioco (verificato nel codice: chiudeva solo i suoi programmi di rete). Quindi la chiusura viene dal client stesso o dai suoi moduli anti-cheat (GameGuard, `mrac64.dll`, `tss_sdk_legacy.dll`).
- Meccanismi tipici: un "mutex" con nome fisso (il secondo avvio trova quello del primo), la ricerca di finestre con la stessa classe, oppure l'anti-cheat che termina le altre istanze.

## Indizi
- Nel patcher: `ArcheAge_SMP` (probabile nome di un oggetto condiviso tra istanze) e la chiave di registro `SOFTWARE\XLGAMES\ArcheAge`. Vedi [[Avvio del client]].

## Piano
1. Osservare il client all'avvio (moduli, finestre, oggetti con nome) e trovare nel codice la funzione che controlla le altre istanze. Richiede il client avviato: vedi [[Themida]], **in attesa del tuo permesso**.
2. Nella **nostra** copia del client: nomi nostri per mutex, classe e titolo della finestra, cartella delle impostazioni separata (ArcheAge scrive in `Documenti\ArcheAge`: due versioni nella stessa cartella si danneggiano a vicenda), eseguibile con nome e icona PonticheAge.
3. Il [[Launcher]] non chiude mai processi fuori dalla cartella PonticheAge e non tocca le altre installazioni.
4. Test: un altro ArcheAge aperto + PonticheAge aperto, entrambi restano vivi per 10 minuti.

## Scoperta (2026-10-07): il caricatore non chiude gli altri
Nel caricatore 10.0.2 il controllo e' solo un mutex `ArcheAge_<suffisso>` con domanda "Do you want to start another one?" ([[Avvio del client]]). Chi chiude gli altri client e' quindi con buona probabilita' il **patcher** o l'**anti-cheat** di un'altra installazione. Il nostro [[Launcher]] non usera' il patcher XLGames; al mutex daremo un nome nostro, cosi' non compare nemmeno la domanda.

## Il semaforo `ArcheAge_SMP` (2026-10-07)
Nel 10.0.2 (`x2game`, `FUN_3991b240`): `CreateSemaphoreA(NULL, 2, 2, "ArcheAge_SMP")` + attesa di 100 ms. Un oggetto di sistema con **2 posti** condiviso da **tutte** le installazioni di ArcheAge: dal terzo client in poi il posto non c'e'. Nel nostro client va rinominato. Siccome `x2game.dll` e' protetta, il modo pulito e' un **addon nostro** che intercetta `CreateSemaphoreA`/`CreateMutexA` e rinomina gli oggetti `ArcheAge_*` in `PonticheAge_*`: niente modifiche ai file protetti.
