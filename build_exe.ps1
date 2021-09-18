#python -m eel main.py ../Frontend/dist --noconsole --onefile !important (use only when u change from project to project) use this first to reload cache compile files

pyinstaller.exe --clean -F -w --icon=icon/icon.ico --onefile main.py
