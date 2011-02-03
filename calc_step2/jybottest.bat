@echo off

set sikuli_jar=C:\Program Files\Sikuli X\sikuli-script.jar

set CLASSPATH=%sikuli_jar%
set JYTHONPATH=%sikuli_jar%/Lib

jybot --pythonpath=calc.sikuli ^
      --outputdir=results ^
      --loglevel=TRACE ^
      %*