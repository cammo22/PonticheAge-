# PonticheAge: regole del progetto

- Obiettivo: server + launcher + addon client per ArcheAge **9.0.2.9 KX r590504**. Niente altre versioni.
- **Clean room**: non copiare ne' adattare codice da AAEmu (GPL-3.0). Fonte di verita' = il client (Ghidra sui moduli estratti dalla memoria) e i suoi dati (game_pak). Se una scorciatoia da AAEmu sembra utile, chiedere prima all'utente.
- Mai mettere in git file del client (`game_pak`, dll, sqlite, dump). Vivono in `_local/` (ignorata).
- La wiki in `wiki/` e' parte del lavoro: ogni scoperta di reverse engineering, decisione o bug risolto va scritta li' (pagina in `wiki/wiki/concepts` o `entities`, voce in `wiki/log.md`, link in `wiki/wiki/index.md`). Formato: frontmatter `tags/type/aliases`, link `[[Pagina]]`.
- Ogni funzione di gioco entra solo con un test automatico (vedi [[Qualita e test]] nella wiki). Niente "funziona, credo".
- Lingua: italiano per wiki, interfacce e messaggi all'utente.
- Il percorso contiene uno spazio: gli script batch (Ghidra) vanno lanciati con il nome corto 8.3 (`cygpath -d`), come fa `tools/ghidra/ghidra.sh`.
- L'utente testa in gioco con istruzioni passo-passo; chiudere i processi rimasti prima di ogni test.
