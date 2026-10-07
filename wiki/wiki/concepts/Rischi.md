---
tags: [rischi, piano]
type: concept
aliases: [Rischi tecnici]
---
# Rischi tecnici

In ordine di gravita'. Ogni rischio ha una verifica in fase 0 o 1.

1. **Client protetto da [[Themida]].** I moduli principali non si leggono da disco. *Piano:* dumper nostro che copia i moduli dalla memoria a client avviato. *Verifica:* stringhe leggibili in Ghidra.
2. **Il client deve partire senza i servizi ufficiali.** GameGuard, `mrac64.dll` (anti-cheat) e `tss_sdk_legacy.dll` potrebbero bloccare l'avvio o il debug. *Piano:* argomenti di avvio stile launcher + DLL sostitutive vuote dove serve. *Verifica:* schermata di login.
3. **Cifratura dei pacchetti.** Ogni versione di ArcheAge cambia chiavi e codici. *Piano:* trovare in `x2game.dll`/`crynetwork.dll` lo scambio di chiavi e la tabella dei codici. *Verifica:* il client finto completa l'handshake con un client vero.
4. **Dati che esistono solo sui server ufficiali** (posizioni dei mostri, loot, IA). *Piano:* cercare gli spawner nei livelli del game_pak; il resto lo progettiamo noi ([[Dati di gioco]]).
5. **Client coreano.** Testi inglesi forse assenti. *Piano:* [[Localizzazione]].
6. **Dimensione del gioco.** E' il rischio di tempo, non tecnico: vedi [[Fattibilita e stima]].
7. **Aspetto legale.** Server privato di un gioco commerciale: uso tra amici, nessun file del client in repository, niente vendita. La repo e' pubblica: contiene solo codice e documentazione nostri.
