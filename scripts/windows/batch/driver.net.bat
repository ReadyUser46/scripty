@echo off

cd C:\Program Files (x86)\Windows Kits\10\Tools\10.0.22621.0\x64
echo Disabling Realtek driver...

devcon disable "PCI\VEN_10EC&DEV_8125&SUBSYS_7D981462&REV_05"
echo Enabling Realtek driver in 3s...

timeout /t 3

devcon enable "PCI\VEN_10EC&DEV_8125&SUBSYS_7D981462&REV_05"
pause
