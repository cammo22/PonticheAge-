---
tags: [client, dlss, ricerca]
type: concept
aliases: [DLSS, DLSS 5]
---
# Upscaling e DLSS 5

**Stato: ricerca, dopo la v1.0.0.** Non promesso.

- DLSS 5 (NVIDIA, uscito il 3 settembre 2026, solo RTX 50) e' "rendering neurale": non solo ingrandisce l'immagine, modifica luce e materiali. Richiede che il gioco gli passi molti dati del fotogramma (profondita', vettori di movimento e altro) tramite le API moderne di NVIDIA.
- Il client 9.0.2.9 disegna con **Direct3D 9/10** (`cryrenderd3d9.dll`, `cryrenderd3d10.dll`). DLSS lavora su D3D11/D3D12/Vulkan.

Percorso possibile, a gradini:
1. Tradurre il rendering in Vulkan (serve anche all'[[Addon prestazioni client]]).
2. Recuperare dal motore profondita' e vettori di movimento (il [[CryEngine 3]] li calcola per il motion blur: da verificare).
3. Prima prova con upscaling classico (DLSS Super Resolution / FSR), poi DLSS 5.

Alternativa subito disponibile senza modificare il gioco: le funzioni del driver NVIDIA (Smooth Motion, upscaling di sistema).
