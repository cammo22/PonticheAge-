---
tags: [architettura, server]
type: concept
aliases: [Architettura]
---
# Architettura del server (proposta)

Principi, nati dai problemi del vecchio progetto ([[Lezioni da DaProd]]):
1. **Un solo processo di gioco.** Niente zone host esterni, niente desktop nascosti, niente processi che si perdono. Le zone sono oggetti dentro il server, ognuna con il suo ciclo di aggiornamento su un pool di thread.
2. **Stato in memoria, database come salvataggio.** Ogni modifica (anche dal pannello) passa da un comando al server vivo, mai da un UPDATE sul database "sotto" al gioco. Cosi' oro, livelli, GM, labor funzionano sempre, online o offline.
3. **Dati del gioco letti dal client**, mai copiati a mano: il database del client e i livelli del game_pak vengono convertiti in un formato nostro veloce al primo avvio ([[Dati di gioco]]).
4. **Regole del gioco come dati.** Moltiplicatori, loot, prezzi, eventi in file di configurazione che il pannello modifica a caldo.
5. **Testabile senza il client.** Il protocollo e' una libreria separata, usata sia dal server sia dal client finto dei test ([[Qualita e test]]).

## Tecnologia
| Parte | Scelta | Perche' |
|---|---|---|
| Server | C# su .NET 10 | Prestazioni ottime, strumenti di profiling/memoria gia' provati, tutto gira su Windows senza installazioni strane |
| Database | PostgreSQL portatile | Robusto con molti salvataggi concorrenti; un solo exe da avviare, gestito dal server |
| Pannello | Web (ASP.NET + interfaccia responsive) servito dal server stesso | Si usa dal browser, anche dal telefono; niente finestre da allargare |
| Launcher | .NET con interfaccia a layout fluido | Vedi [[Launcher]] |
| Addon client | C++ (DLL caricata dal client) | Vedi [[Addon prestazioni client]] |

## Moduli
```
server/
  Ponte.Protocol    pacchetti, cifratura, compressione (condiviso con i test)
  Ponte.Data        lettore game_pak, conversione del database del client
  Ponte.Login       autenticazione, lista server
  Ponte.World       zone, entita', movimento, visibilita'
  Ponte.Game        sistemi di gioco (combattimento, quest, oggetti, ...), uno per cartella
  Ponte.Admin       API per pannello, comandi, regole a caldo
  Ponte.Host        l'exe: avvia database, login, mondo, pannello
tests/
  Ponte.FakeClient  client finto che parla il protocollo vero
```

## Assistente del pannello (opzionale)
[[Needle]] e' un modello minuscolo (8-29 MB) che trasforma frasi in chiamate di funzione. Si puo' usare nel pannello: "dai 500 oro a Speranz", "riavvia alle 4", "chi e' online?" diventano chiamate all'API di `Ponte.Admin`. Gira in locale, senza internet. Fase 5.
