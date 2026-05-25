import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
EMAIL_ADDRESS = os.getenv("VALID_EMAIL")


sections_mapping = {
    "events": "#events",
    "prices": "pricing",
    "tickets": "https://polako-tickets.rs/index-ru.html",
    "certificates": "services",
    "news": "news",
    "about": "about",
    "analytics": "analytics",
}


expected_markers = {
    "telegram": "t.me/polakohedonist",
    "instagram_ru": "instagram.com/polakohedonist/",
    "instagram_sr": "instagram.com/polakohedonist.dogadjaji",
    "email": "mailto:support@polakohedonist.rs",
    "viber": "viber://chat",
    "whatsapp": "whatsapp.com",
}
# LoginPage
TEST_EMAIL = "test3@mail.com"
INVALID_PASSWORD = "WrongPassword123"
UNREGISTERED_EMAIL = "not_exist@test.com"
VALID_TEST_PASSWORD = "Password123"
SQL_INJECTION_PAYLOAD = "' OR 1=1 --"
XSS_PAYLOAD = "<script>alert(1)</script>"
EXPECTED_ERROR_TEXT = "Неверный логин или пароль"
EMPTY_PASSWORD = ""
INVALID_EMAILS = [
    "test",
    "test@",
    "@gmail.com",
    "test.gmail.com",
    "test@com",
]


EVENT_NAME = "test_event"
EVENT_DESCRIPTION = "test_description"
EVENT_LOCATION = "Test Location (NS)"
EVENT_DURATION = "60"
EVENT_COST = "100"
EVENT_TO_DELETE = EVENT_NAME
ROOT_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = ROOT_DIR / "test_data" / "test_events_foto.png"
TITLE_TEXT_RESULT = "The event title is empty."
EXPECTED_EMAIL_FORMAT_ERROR_MESSAGE = (
    "При обновлении пароля произошла ошибка. Попробуйте еще раз."
)
TEST_NAME = "test_name"
VALID_COMPANY_NAME = "Valid Company Name"
LONG_COMPANY_NAME = "A" * 101
EXPECTED_ERROR_TEXT_COMPANY_NAME = "Ошибка: Максимальная длина 100 символов"
COMPANY_REGISTRATION_SUCCESS_MESSAGE = "Компания зарегистрирована"
COOL_BTN_TEXT = "Круто"
SUCCESS_MODAL_MESSAGE = "Информация для смены пароля отправлена на"
