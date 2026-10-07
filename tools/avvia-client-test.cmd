@echo off
rem Avvia il client 9.0.2.9 saltando il patcher XLGames (che resta nero: i server XL non rispondono).
rem Argomenti presi dal patcher stesso: "-y -locale %%s -instant_token %%s".
rem La cartella di lavoro deve essere quella del client (dove sta game_pak), non bin64:
rem altrimenti CrySystem non trova i file di configurazione e mostra "Failed to load commands!".
rem Uso: doppio clic. Facoltativo: avvia-client-test.cmd ko   (lingua coreana invece di en_us)
set LOC=%1
if "%LOC%"=="" set LOC=en_us
cd /d "%~dp0..\_local\client"
start "" "%CD%\bin64\archeage.exe" -y -locale %LOC% -instant_token ponticheage-test
