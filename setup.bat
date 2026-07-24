@echo off
cls
echo ========================================================
echo       Antigravity Hardened Ruleset Suite Auto-Setup
echo ========================================================
echo.
echo This script installs custom model rulesets (including Neon v4.3),
echo skill modules, and the Desktop switcher utility.
echo.
echo Current Repo Path: %~dp0
echo.

set REPO_DIR=%~dp0
set GLOBAL_CONFIG_DIR=%USERPROFILE%\.gemini\config
set DESKTOP_DIR=%USERPROFILE%\Desktop

echo 1. Creating global directories...
if not exist "%GLOBAL_CONFIG_DIR%" mkdir "%GLOBAL_CONFIG_DIR%"
if not exist "%GLOBAL_CONFIG_DIR%\.agents" mkdir "%GLOBAL_CONFIG_DIR%\.agents"
if not exist "%GLOBAL_CONFIG_DIR%\skills\eni" mkdir "%GLOBAL_CONFIG_DIR%\skills\eni"

echo 2. Copying rule files to global configuration...
copy /Y "%REPO_DIR%.agents\*.md" "%GLOBAL_CONFIG_DIR%\.agents\" >nul

echo 3. Copying eni skill files globally...
if exist "%REPO_DIR%.agents\skills\eni" (
    xcopy /Y /E "%REPO_DIR%.agents\skills\eni\*" "%GLOBAL_CONFIG_DIR%\skills\eni\" >nul
)

echo 4. Copying switcher scripts to Desktop...
copy /Y "%REPO_DIR%set-rules.py" "%DESKTOP_DIR%\" >nul
copy /Y "%REPO_DIR%set-rules.bat" "%DESKTOP_DIR%\" >nul

echo 5. Copying master switcher to global configuration...
copy /Y "%REPO_DIR%set-rules.py" "%GLOBAL_CONFIG_DIR%\" >nul

echo 6. Initializing and combining rules globally...
python "%DESKTOP_DIR%\set-rules.py" all

echo.
echo ========================================================
echo Setup Completed Successfully!
echo.
echo Installed Profiles:
echo  - Neon v4.3 (Universal Hardened / Deep Thinking)
echo  - Gemini 3.5 Flash
echo  - Gemini 3.1 Pro
echo  - Claude Sonnet 4.6
echo  - Claude Opus 4.6
echo  - GPT-OSS 120B
echo.
echo Use "set-rules.bat" on your Desktop to swap profiles anytime!
echo ========================================================
echo.
pause
