@echo off
echo.
echo ===== Conversor OFX para Excel =====
echo.
echo Convertendo arquivos OFX para Excel...
echo.

REM Executa o programa ofxcel com os parâmetros corretos
ofxcel.exe ofx -o excel

echo.
echo Conversão concluída!
echo Os arquivos Excel estão disponíveis na pasta "excel"
echo.
pause 