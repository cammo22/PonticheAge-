---
tags: [fonte, storico]
type: source
aliases: [DaProd, DaProdArcheage]
---
# Progetto DaProdArcheage (chiuso)

Primo tentativo, settembre-ottobre 2026: server [[AAEmu]] ramo 10.0.2 con patch, pannello e launcher WinForms, zone in processi separati. Repo `cammo22/DaProdArcheage`, ultima versione 1.11.2. Chiuso il 2026-10-07: vedi [[Lezioni da DaProd]].

Cose utili scoperte allora (da riverificare sul 9.0.2.9):
- Il client accetta argomenti stile launcher (`-StrUserName`, `-strUserToken`, `-serverId`, `-sIp`, `-sPort`, `-gameId`).
- Variabile del client `db_location` per caricare un database alternativo.
- Lingua inglese ottenuta con una patch di `CrySystem.dll` + database con testi `en_us`.
