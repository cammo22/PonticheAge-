@echo off
rem Avvia il client 9.0.2.9 saltando il patcher XLGames (che resta nero: i server XL non rispondono).
rem Argomenti presi dal patcher stesso: "-y -locale %%s -instant_token %%s".
rem Uso: doppio clic. Facoltativo: avvia-client-test.cmd ko   (lingua coreana invece di en_us)
set LOC=%1
if "%LOC%"=="" set LOC=en_us
cd /d "%~dp0..\_local\client\bin64"
start "" archeage.exe -y -locale %LOC% -instant_token ponticheage-test
