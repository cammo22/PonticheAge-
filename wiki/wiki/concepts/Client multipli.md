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
