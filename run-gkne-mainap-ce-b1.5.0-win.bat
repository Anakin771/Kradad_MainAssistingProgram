SET projpath=%~dp0
call :joinpath %projpath% "venv\Scripts\activate.bat"
%Result% && python main.py

:joinpath
set Path1=%~1
set Path2=%~2
if {%Path1:~-1, 1%}=={\} (set Result=%Path1%%Path2%) else (set Result=%Path1%\%Path2%)
goto :eof