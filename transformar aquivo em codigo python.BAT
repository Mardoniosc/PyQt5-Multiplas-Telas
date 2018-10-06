#pyuic5 -x tela_principal.ui -o tela_principal.py

@echo oFF
Mode 78,23
color 1f
echo.
cd %CD%
net session >nul 2>&1

:TOPO
@TITLE Transforma Arquivos .UI em .PY

cls
 echo.
 echo      ฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐ
 echo      ฐฐ                                                               ฐฐ
 echo      ฐฐ ษอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออป ฐฐ
 echo      ฐฐ บ        SCRIPT TRANSFORMAR AQUIVOS UI EM PY                บ ฐฐ
 echo      ฐฐ ศอออออออออออออออออออออออออออออออออออออออออออออออออออออออออออผ ฐฐ
 echo      ฐฐ                                                               ฐฐ
 echo      ฐฐ                                                               ฐฐ
 echo      ฐฐ                                              BY: MARDONIO     ฐฐ
 echo      ฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐฐ
 echo.



set arquivoui=
set /p arquivoui=COLOQUE O NOME DO ARQUIVO UI COM A EXETENSO: 
set arquivopy=
set /p arquivopy=DIGITE O NOME DO ARQUIVO PY DE SAIDA COM EXTENSAO: 

pyuic5 -x %arquivoui% -o %arquivopy%

echo arquivo gerando com sucesso!!
echo.
echo.

@PAUSE