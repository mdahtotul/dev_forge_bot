@echo off
call venv\Scripts\activate
nodemon --watch app --ext py --exec "python main.py"
@REM python main.py
