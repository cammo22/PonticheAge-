---
tags: [home]
type: home
aliases: [Home, Start]
---
# PonticheAge: wiki del progetto

Server, launcher e addon scritti da zero per [[Client AA 9.0.2.9|ArcheAge 9.0.2.9]].

- Indice di tutte le pagine: [[wiki/index|Indice]]
- Diario delle sessioni: [[log]]
- Da dove partire: [[Fattibilita e stima]], [[Roadmap v1.0.0]], [[Architettura server]]

## Come e' organizzato il vault
Il vault segue lo schema "LLM Wiki" di Karpathy ed e' compatibile con il plugin Obsidian **Karpathy LLM Wiki** (gia' installato in `.obsidian/plugins/karpathywiki`):

| Cartella | Cosa contiene |
|---|---|
| `raw/` | Materiale grezzo: dump, tabelle, screenshot, appunti non rielaborati. Non si modifica: si aggiunge. |
| `wiki/sources/` | Una pagina di sintesi per ogni fonte (archivio del client, vecchio progetto, documenti) |
| `wiki/entities/` | Cose concrete: file, programmi, strumenti, moduli del client |
| `wiki/concepts/` | Idee e decisioni: architettura, protocollo, piani, regole |
| `wiki/index.md` | Indice di tutte le pagine |
| `log.md` | Cronologia di cosa e' stato fatto e scoperto |

Per usare l'ingest/Q&A del plugin: Impostazioni > Plugin della community > abilita "Karpathy LLM Wiki", scegli il provider (Anthropic) e la lingua **Italiano**. Il plugin scrive nelle stesse cartelle.
