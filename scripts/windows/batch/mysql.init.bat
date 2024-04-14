@echo off
sc query MySQL80 | find "RUNNING" > nul
if errorlevel 1 (
    echo Initializing process 'MySQL80'...
    net start MySQL80
) else (
    echo The process 'MySQL80' is being already executed.
)

pause
