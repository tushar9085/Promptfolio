@echo off
rem ===========================================================================
rem  Promptfolio Runner for Windows
rem ===========================================================================
rem  This script starts both the backend and frontend servers for the 
rem  Promptfolio application in separate terminal windows.
rem ===========================================================================

title Promptfolio Runner

echo --------------------------------------------------
echo           Starting Promptfolio Servers
rem --------------------------------------------------
echo.
echo IMPORTANT:
rem - Make sure you have installed all dependencies first by running:
rem   - pip install -r requirements.txt
rem   - cd Frontend\Promptfolio && npm install
rem - Ensure your API key is set in 'API\.env'
echo.

rem Start the backend server in a new window
echo Starting Backend Server...
start "Promptfolio Backend" cmd /k "echo Activating backend environment... && .\API\env\Scripts\activate && echo Starting FastAPI server... && uvicorn API.main:app --reload"

rem Start the frontend server in a new window
echo Starting Frontend Server...
start "Promptfolio Frontend" cmd /k "echo Navigating to frontend directory... && cd Frontend\Promptfolio && echo Starting Vite dev server... && npm run dev"

echo.
echo --------------------------------------------------
echo   Servers are launching in new windows.
rem --------------------------------------------------
echo.
echo Your application will be available at:
rem http://localhost:5173
echo.
echo You can close this window.

pause
