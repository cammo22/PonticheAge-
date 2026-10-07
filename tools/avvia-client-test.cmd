@echo off
rem Avvia il client 9.0.2.9 come fa il patcher XLGames, senza patcher:
rem   archeage.exe <16 caratteri con IP/porta del login> -y -locale <lingua> -instant_token <token>
rem Il codice di 16 caratteri lo genera tools\launch\cmdline.py (vedi wiki "Avvio del client").
rem Senza quel codice il gioco mostra "Failed to load commands!".
rem Uso: doppio clic (login 127.0.0.1:1237). Facoltativo: avvia-client-test.cmd <ip> <porta>
set IP=%1
if "%IP%"=="" set IP=127.0.0.1
set PORT=%2
if "%PORT%"=="" set PORT=1237
for /f "delims=" %%a in ('python "%~dp0launch\cmdline.py" --ip %IP% --port %PORT% "--mode=-y -locale en_us -instant_token ponticheage-test"') do set ARGS=%%a
if "%ARGS%"=="" (echo Python non trovato o errore nel generatore. & pause & exit /b 1)
cd /d "%~dp0..\_local\client"
echo Avvio: archeage.exe %ARGS%
start "" "%CD%\bin64\archeage.exe" %ARGS%
