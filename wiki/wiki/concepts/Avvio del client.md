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

### Seconda prova: stesso errore anche dalla cartella giusta
Non si crea nessun file (niente `ArcheAge.log`): il client muore prima di scrivere log. La cartella di lavoro non era quindi la causa (o non l'unica).

### Il caricatore `archeage.exe` (dal 10.0.2 non protetto, `_local/re/out/loader10.c`)
1. **Istanze**: crea il mutex `ArcheAge_<suffisso>`; se esiste gia', chiede "There is already a x2client application running / Do you want to start another one?" (Si' = continua). **Non chiude** nulla.
2. Se ha meno di 1 argomento: avvia `bin32\patcher.exe` ("restarting patcher...") e si chiude. Ecco perche' il doppio clic apre il patcher.
3. `XlSetWorkingDir`, poi crea un collegamento (junction) `Documents` che punta a `Documenti\ArcheAge`: tutte le installazioni condividono quella cartella.
4. Opzioni: `-reset_env` / `-reset_env_s` (svuota la cartella dei salvataggi!), `-devmode` (carica `x2game-dev.dll`, anche da `devmode.cfg`), `-fulldump`.
5. Carica `x2game.dll` e chiama `CreateGameStartup`.
Attenzione: il 10.0.2 e' la build cinese ("shanggushiji" nel percorso del pdb), il 9.0.2.9 e' coreano: nel 9.0.2.9 il collegamento `Documents` non viene creato, quindi il caricatore e' diverso.

### Prossimo passo
Quando compare "Failed to load commands!" il processo resta vivo finche' non si preme OK, con i moduli gia' decifrati e GameGuard non ancora partito: e' il momento giusto per il dumper (`tools/dumper/dump_modules.py`, aggiornato con argomenti e cartella giusti). In attesa dell'utente.


## RISOLTO: "Failed to load commands!" (2026-10-07)
Causa: mancava il **primo argomento**. Il patcher (`FUN_00490670`) costruisce la riga di comando cosi':
```
archeage.exe <16 caratteri> -y -locale <lingua> -instant_token <token>
```
I 16 caratteri sono i "commands": 12 byte con **IP e porta del server di login**, 4 byte casuali, un checksum e un flag, in XOR con una chiave e codificati con il base64 di `xlcommon.dll` (alfabeto `./0-9A-Za-z`). Dettagli e codice: `tools/launch/cmdline.py` (con test andata/ritorno).
Altre modalita' viste nel patcher: `-k [chiave]` (in questo client si chiude subito, codice 0) e `-j a|b|c|d|e|f|g h`.

### Cosa fa il client con la riga giusta (prova del 2026-10-07)
| Secondi | Evento |
|---|---|
| ~1 | carica `crysystem`, `cryaction`; poi rete, suono, grafica (D3D9) |
| ~44 | finestra "- ArcheAge - 9.0.2.9.KX (r.590504) Sep 21 2022 (11:18:58)" |
| ~60 | carica la scena di login `loginbg4` |
| ~64 | collegamento HTTPS a `52.9.67.121:443` (`ec2-52-9-67-121.us-west-1.compute.amazonaws.com`): telemetria o anti-cheat XLGames, **da bloccare** nel nostro client |
| ~66 | si collega al **nostro** IP:porta di login |
| senza server | si chiude con codice 1 |

`tools/avvia-client-test.cmd` ora genera da solo la riga giusta (richiede Python).

## Primo pacchetto di login (2026-10-07)
Catturato con `tools/launch/sniff_login.py` (copia in `raw/login_first.bin`). 55 byte, **in chiaro**:
```
35 00 15 00 0a 00 00 00 08 00 00 00 00 00 08 00
00 00 00 00 00 00 00 00 08 00 74 56 3c b6 ee a0
00 00 10 00 70 6f 6e 74 69 63 68 65 61 67 65 2d   ....ponticheage-
74 65 73 74 01 00 01                              test...
```
- `35 00` lunghezza (53 byte dopo questo campo), `15 00` tipo di pacchetto 0x15
- `0a 00 00 00` = 10: lo stesso valore che il patcher scrive per i token istantanei
- campi da 8 byte con lunghezza `08 00` (uno vuoto, uno `74 56 3c b6 ee a0 00 00`: forse un identificativo della macchina)
- `10 00` + `ponticheage-test`: il nostro token
- coda `01 00 01`
Significato preciso dei campi: da confermare quando avremo `x2game.dll` estratta. Vedi [[Protocollo di rete]].
