import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    VALID_EMAIL = os.getenv("VALID_EMAIL")
    VALID_PASSWORD = os.getenv("VALID_PASSWORD")
    STG_URL = os.getenv("STG_URL")
    PROD_URL = os.getenv("PROD_URL")
    CARD_NUMBER = os.getenv("CARD_NUMBER")
    EXP_MONTH = os.getenv("EXP_MONTH")
    EXP_YEAR = os.getenv("EXP_YEAR")
    SVV_CODE = os.getenv("SVV_CODE")
    PROMO10 = os.getenv("PROMO10")
    PROMO20 = os.getenv("PROMO20")
    PROMO30 = os.getenv("PROMO30")
    AUTH_TOKEN = os.getenv("AUTH_TOKEN")

    @classmethod
    def validate(cls):

        required = ["STG_URL", "CARD_NUMBER", "SVV_CODE"]
        for var in required:
            if not getattr(cls, var):
                raise ValueError(f"Error: Environment variable {var} is not set in .env!")