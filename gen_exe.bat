@ECHO OFF
pyinstaller -F utfdir.py
rd /s /q build
rd /s /q __pycache__
move dist\utfdir.exe utfdir.exe
rd /s /q dist
del utfdir.spec