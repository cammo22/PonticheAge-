---
tags: [client, dlss, ricerca]
type: concept
aliases: [DLSS, DLSS 5]
---
# Upscaling e DLSS 5

**Stato: strada concreta trovata (2026-10-07), da provare quando il client gira.**

## Il problema
- DLSS 5 (NVIDIA, 3 settembre 2026) e' "rendering neurale": modifica luce e materiali, non solo la risoluzione. Ufficialmente si aggancia solo ai giochi che chiamano gia' DLSS.
- Il client 9.0.2.9 disegna con Direct3D 9/10 e non ha DLSS.

## I progetti della comunita' (GitHub)
| Progetto | Cosa fa | Note per noi |
|---|---|---|
| **DLSS5-Feeder** (jlrouzies-fr) | Fa lui le chiamate DLSS che il gioco non fa: prende da ReShade immagine, profondita' e vettori di movimento stimati e lancia DLSS DLAA + il passaggio neurale | Dichiara supporto anche per **DirectX 9 e 10**: e' la strada per ArcheAge |
| **DLSS 5 Swapper** (rakanki911, MIT, ~7900 stelle) | Installa/ripristina con un clic Feeder, RenoDX, OptiScaler, ReShade; dgVoodoo2 per DX8/9 -> DX11; overlay F8 | Utile come riferimento per l'installazione automatica dal nostro [[Launcher]] |
| **OptiScaler** | Scambia DLSS/FSR/XeSS nei giochi che ne hanno gia' uno | DX11/12/Vulkan: non serve direttamente |
| FeedKit, dlss5-enabler, DLSS5-Everything | Installer alternativi per Feeder | Riferimento |

## Limiti onesti
- **La tua scheda e' una RTX 4060.** Il modello neurale di NVIDIA parte ufficialmente solo sulle RTX 50: su RTX 20/30/40 DLSS funziona ma il passaggio neurale no. I progetti usano una `nvngx_dlssnr.dll` **modificata**, distribuita fuori da GitHub: non la includiamo nei nostri pacchetti. Su RTX 4060 quindi si puo' contare su **DLSS DLAA / Super Resolution**, mentre il neurale resta da verificare.
- I vettori di movimento sono **stimati** da ReShade, non calcolati dal motore: possibili scie sugli oggetti veloci. Miglioria futura: prenderli dal motore ([[CryEngine 3]] li calcola per il motion blur, da verificare in `cryrenderd3d10.dll`, che non e' protetto).
- Alcune guide parlano di una build DLSS 5 "trapelata": usiamo solo file ufficiali NVIDIA.

## Piano
1. Quando il client parte: ReShade + DLSS5-Feeder sulla **nostra** copia del client, misura di qualita' e fps.
2. Se funziona: il [[Launcher]] lo installa e lo aggiorna da solo, con un interruttore "DLSS" nelle impostazioni.
3. Poi i vettori di movimento veri dal motore.
