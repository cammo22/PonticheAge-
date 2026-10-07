---
tags: [requisiti, lezioni]
type: concept
aliases: [Problemi vecchio progetto, Requisiti]
---
# Lezioni dal vecchio progetto

Problemi segnalati sul [[Progetto DaProdArcheage]] (2026-10-07). Ognuno diventa un **requisito con test** della nuova versione.

| Problema | Causa probabile nel vecchio progetto | Requisito nuovo |
|---|---|---|
| Gli NPC spariscono quando sali su una cavalcatura | Il mate non veniva annunciato alla zona; zone separate in processi diversi | Cavaliere e cavalcatura sono la stessa entita' per la visibilita'. Test: salire/scendere, gli NPC restano visibili |
| Livelli ancestrali assenti | Mai implementati per quel client | Ancestrali completi in fase 2 |
| Potenziamento bloccato al rank 3, Hiram unique non arriva a Celestial | Lettura sbagliata dei costi di grado, tabelle di una versione diversa | Gradi letti dalla tabella del client 9.0.2.9; test per ogni grado di ogni famiglia di equipaggiamento |
| Testi in coreano/cinese | Il database del client era coreano; traduzioni incomplete | [[Localizzazione]]: copertura misurata al 100% delle stringhe visibili |
| Pannello e launcher non responsive, pulsanti fuori schermo, manca "aggiorna" | Finestre WinForms a larghezza fissa | Pannello web responsive, aggiornamento automatico + pulsante; launcher a layout fluido |
| "/annulla" come comando chat (annullava l'effetto di un'arma) | Non si era riusciti a mettere un pulsante nell'interfaccia | Pulsante **in gioco**, vedi [[Regole personalizzate]] |
| Altri ArcheAge del PC si chiudono | Controllo delle istanze nel client/anti-cheat | [[Client multipli]] |
| Pass: missioni date a ogni login ma non si aggiornano, non ne escono di nuove | Stato del pass mai inviato in modo coerente | Pass con stato persistente, avanzamento in tempo reale, rotazione delle missioni; test a orologio simulato |
| Daily rotte | Quest "auto-complete" rimaste in Ready | Daily/settimanali con reset all'orario giusto; test a orologio simulato |
| Onore e vocazione non spendibili | Negozi e valute non collegati | Negozi a valuta collegati al saldo vero; test di acquisto |
| "Sembra tutto corrotto" | Server di un'altra versione (10.0.2) con patch sopra; zone in processi esterni | Un solo server, una sola versione, nessuna patch su codice altrui ([[Architettura server]]) |

Nota tecnica: il vecchio server era il ramo AAEmu **10.0.2**, mentre il client di riferimento ora e' il **9.0.2.9**. Molti problemi venivano da questo disallineamento.
