@echo off
setlocal enabledelayedexpansion

:: Check if Python 3.11+ is installed
python --version 2>NUL
if errorlevel 1 (
    echo Error: Python 3.11 or higher is required.
    exit /b 1
)

:: Check if Poetry is installed
poetry --version 2>NUL
if errorlevel 1 (
    echo Error: Poetry is required. Please install it first.
    exit /b 1
)

:: Install URS
echo Installing URS...
git clone --depth=1 https://github.com/JosephLai241/URS.git
cd URS
poetry install
poetry run maturin develop --release

:: Install Manhwa Analyzer CLI
echo Installing Manhwa Analyzer CLI...
cd ..
git clone https://github.com/your_username/manhwa_analyzer.git
cd manhwa_analyzer
poetry install

:: Add CLI to PATH
set "CLI_DIR=%cd%"
setx PATH "%PATH%;%CLI_DIR%"

echo Installation complete!
echo Please restart your command prompt to update your PATH.

endlocal