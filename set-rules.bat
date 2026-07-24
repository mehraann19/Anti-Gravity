@echo off
:menu
cls
echo ===================================================
echo     Antigravity Hardened Ruleset Suite Switcher
echo ===================================================
echo.
echo Select the ruleset to apply:
echo.
echo  [1] Neon v4.3 (Universal Hardened / Deep Thinking)
echo  [2] Gemini 3.5 Flash (High/Medium/Low)
echo  [3] Gemini 3.1 Pro (Low/High)
echo  [4] Claude Sonnet 4.6 (Thinking)
echo  [5] Claude Opus 4.6 (Thinking)
echo  [6] GPT-OSS 120B (Medium)
echo  [7] Combine ALL models (Unified AGENTS.md)
echo  [8] Exit
echo.
echo ===================================================
set /p choice="Enter choice [1-8]: "

if "%choice%"=="1" goto neon
if "%choice%"=="2" goto flash
if "%choice%"=="3" goto pro
if "%choice%"=="4" goto sonnet
if "%choice%"=="5" goto opus
if "%choice%"=="6" goto gpt
if "%choice%"=="7" goto all
if "%choice%"=="8" goto end

echo.
echo Invalid selection. Please enter a number between 1 and 8.
echo.
pause
goto menu

:neon
echo.
python "%USERPROFILE%\Desktop\set-rules.py" neon
echo.
pause
goto menu

:flash
echo.
python "%USERPROFILE%\Desktop\set-rules.py" flash
echo.
pause
goto menu

:pro
echo.
python "%USERPROFILE%\Desktop\set-rules.py" pro
echo.
pause
goto menu

:sonnet
echo.
python "%USERPROFILE%\Desktop\set-rules.py" sonnet
echo.
pause
goto menu

:opus
echo.
python "%USERPROFILE%\Desktop\set-rules.py" opus
echo.
pause
goto menu

:gpt
echo.
python "%USERPROFILE%\Desktop\set-rules.py" gpt
echo.
pause
goto menu

:all
echo.
python "%USERPROFILE%\Desktop\set-rules.py" all
echo.
pause
goto menu

:end
echo.
echo Goodbye!
echo.
exit
