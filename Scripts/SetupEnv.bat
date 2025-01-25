@echo off
echo Changing directory to parent...
cd ..

echo Creating virtual environment...

:: Check if venv exists, if not, create one
if not exist "env" (
    python -m venv env
)

echo Activating virtual environment...
call env\Scripts\activate.bat

echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

echo Environment setup complete. You can now activate it and start working.

pause
