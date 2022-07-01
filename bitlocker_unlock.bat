@echo off
:start
cls
echo =====================================================================
echo        ---------------------------------------------------
echo        -  D R I V E   U N L O C K E R   by  Qu3st10nm4rk -
echo        ---------------------------------------------------
echo =====================================================================
 
set /p IN= Enter Drive Letter or 'q' to quit : 

if %IN%==E (goto unlockE)
if %IN%==F (goto unlockF)
if %IN%==D (goto unlockD)
if %IN%==q (goto terminate)

:unlockE

manage-bde E: -unlock -password
goto start

:unlockF
manage-bde F: -unlock -password
goto start

:unlockD
manage-bde D: -unlock -password
goto start

:terminate
cls
exit