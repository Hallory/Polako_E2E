from typing import Any, Dict
from urllib.parse import urlparse

import requests


def _extract_access_token(response_data: Dict[str, Any]) -> str | None:
    return (
        response_data.get("data", {}).get("access_token")
        or response_data.get("access_token")
        or response_data.get("token")
    )


def _session_cookies_for_playwright(
    session: requests.Session, base_url: str
) -> list[dict[str, Any]]:
    parsed_url = urlparse(base_url)
    hostname = parsed_url.hostname
    if not hostname:
        raise ValueError(f"Invalid base_url: {base_url}")

    cookies = []
    for cookie in session.cookies:
        cookies.append(
            {
                "name": cookie.name,
                "value": cookie.value,
                "domain": cookie.domain or hostname,
                "path": cookie.path or "/",
                "expires": cookie.expires or -1,
                "httpOnly": "HttpOnly" in cookie._rest,
                "secure": cookie.secure,
                "sameSite": cookie._rest.get("SameSite", "Lax"),
            }
        )
    return cookies


def get_api_auth_state(base_url: str, email: str, password: str) -> Dict[str, Any]:
    base_api_url = base_url.replace("/en", "").rstrip("/")
    session = requests.Session()

    login_response = session.post(
        f"{base_api_url}/api/auth/login",
        json={"email": email, "password": password, "mode": "cookie"},
        timeout=30,
    )
    login_response.raise_for_status()

    login_data = login_response.json()
    refresh_response = session.post(
        f"{base_api_url}/api/auth/refresh",
        json={"mode": "cookie"},
        timeout=30,
    )
    refresh_response.raise_for_status()
    refresh_data = refresh_response.json()

    access_token = _extract_access_token(refresh_data) or _extract_access_token(
        login_data
    )

    if not access_token:
        raise Exception(
            f"No token in responses: login={login_data}, refresh={refresh_data}"
        )

    return {
        "access_token": access_token,
        "cookies": _session_cookies_for_playwright(session, base_url),
    }


def get_api_token(base_url: str, email: str, password: str) -> str:
    return get_api_auth_state(base_url, email, password)["access_token"]


def create_event_api(
    base_url: str, token: str, event_data: Dict[str, Any]
) -> Dict[str, Any]:
    base_api_url = base_url.replace("/en", "").rstrip("/")
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    response = requests.post(
        f"{base_api_url}/api/events", json=event_data, headers=headers, timeout=30
    )
    response.raise_for_status()
    return response.json()


def delete_event_api(base_url: str, token: str, event_id: str) -> Dict[str, Any]:
    base_api_url = base_url.replace("/en", "").rstrip("/")
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    response = requests.post(
        f"{base_api_url}/api/events/{event_id}/delete", headers=headers, timeout=30
    )
    response.raise_for_status()
    return response.json() if response.text else {}


def event_exists_api(base_url: str, token: str, event_id: str) -> bool:
    base_api_url = base_url.replace("/en", "").rstrip("/")
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    response = requests.get(
        f"{base_api_url}/api/events/{event_id}", headers=headers, timeout=30
    )
    return response.status_code == 200
