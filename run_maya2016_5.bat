@echo off
set ECO_ROOT=%~dp0Ecosystem/ecosystem
set ECO_ENV=%~dp0env
set PATH=C:/Python27;%PATH%

python ./Ecosystem/ecorun.py -t base,Qt.py,maya2016.5,spaceSwitcher1.0.0 -r maya
