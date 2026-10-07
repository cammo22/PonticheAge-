---
tags: [client, avvio]
type: concept
aliases: [Avvio, Patcher, Argomenti di avvio]
---
# Avvio del client

## Cosa succede con il doppio clic su `archeage.exe`
Senza argomenti `archeage.exe` apre il **patcher XLGames** (`bin32/patcher.exe`, finestra "ArcheAge Patcher"). La sua interfaccia e' una pagina web (CEF) dei server XLGames, che non rispondono piu': **schermata nera** e il log `Documenti\ArcheAge\Patcher.log` si riempie di `P2WSetConfig is not defined`. Crea `patch_data/` (vuota) e `GPUCache/` nel client, nient'altro. Provato dall'utente il 2026-10-07.

## Argomenti del gioco vero
Il patcher (non protetto) contiene il formato con cui lancia il gioco:
```
archeage.exe -y -locale <lingua> -instant_token <codice>
```
- `-y`: avvio dal patcher (salta l'aggiornamento)
- `-locale`: lingua (`en_us`, `ko`, ...)
- `-instant_token`: codice di accesso che il client manda al server di login: sara' il **nostro** [[Launcher]] a generarlo e il nostro server a verificarlo.

File di prova: `tools/avvia-client-test.cmd` (doppio clic; opzionale `ko`).

### "Failed to load commands!" (2026-10-07)
Primo tentativo: finestra "ArcheAge Error / Failed to load commands!" e chiusura immediata, nessun `ArcheAge.log`.
- Il messaggio sta in `crysystem.dll` (nel 10.0.2 non protetto: funzione `FUN_365e2310`, MessageBox + TerminateProcess, chiamata solo in modo indiretto).
- Le stringhe accanto sono quelle del caricamento dei file di configurazione (`exec`, "executes a batch file of console commands", `game/`, `config/`, `game/config/`): il client non trovava i suoi file.
- Causa probabile: lo script avviava il gioco con cartella di lavoro `bin64`; il patcher invece parte dalla cartella principale (`%sin32rcheage.exe`), dove sta `game_pak`. Script corretto: `cd` nella cartella del client, poi `bin64rcheage.exe`.

## Altre stringhe utili nel patcher
- `ArcheAge_SMP`: candidato per il nome dell'oggetto che il client usa per riconoscere le altre istanze → [[Client multipli]].
- `SOFTWARE\XLGAMES\ArcheAge`: chiave di registro condivisa tra installazioni → da separare per PonticheAge.
- `ERROR: failed to find GameOn Launcher Window.`, `webLauncher`, `instanceToken`, `SetLoginKey`, `authSVC`: flusso del launcher web XLGames.
- Il patcher scarica con torrent (libtorrent) e curl; usa `/master/bin64/`, `/master/bin32/`.

## Nota: cartella Documenti condivisa
`Documenti\ArcheAge` e' usata da **tutte** le installazioni di ArcheAge del PC (ci sono anche log di altri client del 6 ottobre). Il Patcher.log di prima e' stato sovrascritto. PonticheAge dovra' usare una cartella sua ([[Client multipli]]).
