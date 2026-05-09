import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

BASE_URL = os.getenv("BASE_URL", "https://stg.polakohedonist.club/ru")

MANAGER_EMAIL = os.getenv("MANAGER_EMAIL", "")
MANAGER_PASSWORD = os.getenv("MANAGER_PASSWORD", "")