---
tags: [lingua, traduzione]
type: concept
aliases: [Traduzione, Lingua, Testi]
---
# Localizzazione

Il client e' coreano (KX). Obiettivo: **tutta** l'interfaccia in inglese (e, se vuoi, italiano), senza una sola stringa in coreano o cinese.

Piano:
1. Estrarre le tabelle dei testi del database del client e misurare quante righe hanno gia' l'inglese.
2. Riempire i buchi con i testi del database multilingua 10.0.2 (stesso id).
3. Il resto: traduzione automatica dal coreano, poi rilettura delle parti visibili.
4. Testi fissi nell'interfaccia Lua e nelle DLL `res_*.dll`: estrazione e sostituzione.
5. Test: script che scorre tutte le stringhe mostrate dal client e fallisce se trova caratteri coreani/cinesi.

Lingua del client: il vecchio progetto la cambiava con una patch di `CrySystem.dll`; per il 9.0.2.9 va ritrovato il punto equivalente.
