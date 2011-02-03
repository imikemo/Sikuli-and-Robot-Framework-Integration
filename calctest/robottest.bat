@echo off

set sikuli_jar=C:\Program Files\Sikuli X\sikuli-script.jar

java -cp "robotframework-2.5.5.jar;%sikuli_jar%" ^
     -Dpython.path="%sikuli_jar%/Lib" ^
     org.robotframework.RobotFramework ^
     --pythonpath=CalcLib ^
     --outputdir=results ^
     --loglevel=TRACE ^
     %*