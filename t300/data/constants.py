import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

BASE_URL = os.getenv("BASE_URL", "https://stg.polakohedonist.club/en")

MANAGER_USER = {
    "email": os.getenv("MANAGER_EMAIL"),
    "password": os.getenv("MANAGER_PASSWORD"),
}
