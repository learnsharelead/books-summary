@echo off
echo ========================================
echo  BookWise - AI-Powered Book Summaries
echo ========================================
echo.

REM Check if venv exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate venv
call venv\Scripts\activate

REM Install dependencies
echo Installing dependencies...
pip install -q -r requirements.txt

REM Initialize database
echo Seeding database...
python -m database.seed

REM Run Streamlit
echo.
echo Starting BookWise...
echo Access at: http://localhost:8501
echo.
streamlit run Home.py
