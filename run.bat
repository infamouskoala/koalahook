@echo off
echo Installing dependecies...
pip install -r requirements.txt
cls
echo Running KoalaHook...
timeout /t 2
py koalahook.py
