---
tags: [protocollo, rete, reverse-engineering]
type: concept
aliases: [Protocollo, Pacchetti, Opcode]
---
# Protocollo di rete (9.0.2.9)

> Stato: **da ricavare**. Niente qui e' ancora verificato sul client 9.0.2.9.

## Come lo ricaviamo
1. Dump di `x2game.dll` e `crynetwork.dll` dalla memoria ([[Themida]]).
2. In [[Ghidra]]: le classi dei pacchetti hanno nomi leggibili nelle stringhe/RTTI (es. `CSxxx` client->server, `SCxxx` server->client). Da li': costruttore, codice numerico, funzione di lettura/scrittura campo per campo.
3. Script Ghidra che esporta **tutta la tabella** (nome, codice, campi) in `raw/protocol/`, da cui generiamo automaticamente il codice C# di `Ponte.Protocol`.
4. Handshake e cifratura: si seguono `send`/`recv` di Winsock in `crynetwork.dll` fino alle routine di cifratura.
5. Verifica: [[Qualita e test]] livello 2.

## Da annotare qui, man mano
- Porte e sequenza di login
- Formato dell'intestazione (lunghezza, tipo, compressione)
- Algoritmo e chiavi di cifratura
- Tabella dei codici (link al file generato)
