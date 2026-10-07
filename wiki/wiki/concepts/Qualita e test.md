---
tags: [qualita, test]
type: concept
aliases: [Test, Zero bug]
---
# Qualita' e test

"Nemmeno un bug" in pratica significa: **nessuna funzione entra senza la prova che funziona, e nessun bug torna due volte.**

## Livelli di test
1. **Unitari**: formule, gradi, costi, loot, orari di reset (con orologio simulato).
2. **Protocollo**: ogni pacchetto si scrive e si rilegge identico; i pacchetti catturati dal client vero si decodificano senza byte avanzati.
3. **Scenari con client finto** (`Ponte.FakeClient`): "login, crea personaggio, entra, monta, cammina 200 m, gli NPC sono ancora visibili". Girano a ogni modifica, in automatico su GitHub.
4. **In gioco**: tu, con istruzioni passo-passo e una checklist per ogni rilascio.

## Regole
- Ogni bug segnalato: prima un test che lo riproduce, poi la correzione.
- Rilascio solo con tutti i test verdi e la checklist di gioco completata.
- I log del server sono strutturati e leggibili dal pannello, con un pulsante "segnala problema" che raccoglie log e stato.
