---
tags: [client]
type: entity
aliases: [Client 9.0.2.9, ArcheAge 9.0.2.9, r590504]
---
# Client ArcheAge 9.0.2.9

- Versione: **9.0.2.9 KX**, XLGames, revisione **r590504**, compilato il 2022-09-21 (data nei PE).
- Posizione: `_local/client` (52,8 GB): `bin64/`, `bin32/`, `game_pak` (49,6 GB). Fonte: [[Archivio client 9.0.2.9]].
- Rendering: Direct3D 9 e Direct3D 10 (`cryrenderd3d9.dll`, `cryrenderd3d10.dll`), [[CryEngine 3]].
- Protezioni: [[Themida]] su `archeage.exe`, `x2game.dll`, `crynetwork.dll`, `crysystem.dll`; GameGuard (`bin64/GameGuard`), `mrac64.dll` (anti-cheat, 65 MB), `tss_sdk_legacy.dll`, `secureenginesdk64.dll`.
- Altro: Chromium Embedded (`libcef.dll`) per le pagine web in gioco, Steam API, FMOD per l'audio, `tbbmalloc`.
- Configurazioni: `archeagekr.ini`, `archeagejptest.ini`.

## Moduli
| Modulo | Ruolo | Protetto |
|---|---|---|
| `x2game.dll` (11,8 MB) | Logica del gioco, pacchetti, interfaccia Lua | si |
| `crynetwork.dll` | Rete | si |
| `crysystem.dll` | Avvio motore, variabili, lingua | si |
| `cry3dengine.dll` | Mondo, streaming | no |
| `cryrenderd3d9/10.dll` | Rendering | no |
| `cryphysics.dll`, `cryanimation.dll`, `cryaction.dll`, `cryentitysystem.dll` | Motore | no |
