---
tags: [piano, roadmap]
type: concept
aliases: [Roadmap, Piano]
---
# Roadmap fino alla v1.0.0

Tempi e motivazioni: [[Fattibilita e stima]]. Ogni voce si spunta solo quando ha un test automatico ([[Qualita e test]]) e l'hai provata in gioco.

## Fase 0: fondamenta (in corso)
- [x] Cartella e repo nuove, wiki
- [x] Client 9.0.2.9 estratto in `_local/client`
- [x] Ghidra, JDK, Universal Modder, REA in `_local/tools`
- [ ] Il client parte in locale fino alla schermata di login (GameGuard/anti-cheat: vedi [[Client AA 9.0.2.9]]) — **in attesa del permesso dell'utente**
- [ ] Identita' separata del client: non chiude gli altri ArcheAge ([[Client multipli]])
- [ ] Dumper nostro (scritto: `tools/dumper/dump_modules.py`, mai eseguito): copia `x2game.dll`, `crynetwork.dll`, `crysystem.dll` dalla memoria del client avviato e ricostruisce i PE leggibili da Ghidra ([[Themida]])
- [ ] Analisi Ghidra dei moduli estratti: stringhe, funzioni Lua, tabella dei pacchetti
- [ ] Lettore del `game_pak` (formato e chiavi) e estrazione del database del client ([[Dati di gioco]])
- [ ] Mappa del protocollo: handshake, cifratura, compressione, elenco dei codici ([[Protocollo di rete]])
- [ ] Scheletro del server .NET ([[Architettura server]]) + client finto per i test + build automatica su GitHub

## Fase 1: entrare nel mondo
- [ ] Login e lista server; account e password sul nostro database
- [ ] Creazione, cancellazione e selezione personaggio
- [ ] Ingresso nel mondo, caricamento zona, movimento, salto, nuoto, caduta
- [ ] Visibilita' tra giocatori (aree di interesse), chat (vicini, gruppo, mondo, sussurri)
- [ ] Launcher nuovo ([[Launcher]]) con aggiornamenti automatici
- [ ] **v0.1**

## Fase 2: gioco base
- [ ] Statistiche, formule, combattimento, skill, buff/debuff, cooldown
- [ ] NPC, mostri, IA, aggro, respawn; spawner dai livelli del game_pak (se presenti)
- [ ] Loot, esperienza, livelli 1-55, **livelli ancestrali**
- [ ] Inventario, banca, equipaggiamento, gradi, potenziamento e risveglio; Hiram fino a Celestial e oltre
- [ ] Sintesi con Serendipity Stone a scelta diretta, pulsante per annullare l'effetto dell'arma ([[Regole personalizzate]])
- [ ] Quest (storia, secondarie, ripetibili)
- [ ] Testi tutti in inglese/italiano ([[Localizzazione]])
- [ ] **v0.5**

## Fase 3: vita ed economia
- [ ] Raccolta, crafting, ricettari, lavoro (labor)
- [ ] Case, fattorie, permessi, tasse
- [ ] Trade pack e mercati
- [ ] Posta, asta, negozio, valute (onore, vocazione) spendibili
- [ ] Pass stagionale con missioni che si aggiornano davvero; daily/settimanali che si rinnovano
- [ ] **v0.8**

## Fase 4: mondo vivo
- [ ] Cavalcature, mate, pet (con gli NPC che restano visibili quando monti)
- [ ] Navi e veicoli, mare
- [ ] Gilde, famiglie, gruppi, raid
- [ ] Dungeon e istanze, arene, PvP, fazioni
- [ ] Castelli, assedi, boss mondiali, eventi

## Fase 5: rifinitura e rilascio
- [ ] [[Addon prestazioni client]]
- [ ] [[Pannello server]] web, responsive, utilizzabile anche dal telefono
- [ ] Beta chiusa con gli amici, correzione dei bug trovati
- [ ] **v1.0.0**

## Dopo la 1.0
- [[Upscaling e DLSS 5]]
- Modifiche profonde al gioco (nuovi sistemi, bilanciamento nostro)
