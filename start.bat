@echo off
set PATH=%PATH%;%~dp0\python;
echo ****************************************
echo XX-Net-mini
echo ****************************************
echo.
ver
wmic computersystem get systemtype
echo.
title XX-Net-mini
echo.
openssl version
python -V
echo.
cd .\code\default\launcher && python start.py





