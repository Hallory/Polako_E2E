import os
from pathlib import Path

from TP_Polako_E2E.api.base_api import BaseApi


class AuthApi(BaseApi):
    def login_and_save_token(self, email: str, password: str) -> str:
        response = self.session.post(
            f"{self.base_url}/api/auth/login",
            json={"email": email, "password": password},
        )
        response.raise_for_status()

        token = response.json().get("data", {}).get(
            "access_token"
        ) or response.json().get("access_token")

        if token:
            self.session.headers.update({"Authorization": f"Bearer {token}"})
            self.save_token_to_env(token)

        return token

    def save_token_to_env(self, token: str):
        env_path = Path(__file__).resolve().parent.parent / ".env"
        token_line = f"AUTH_TOKEN={token}\n"

        if env_path.exists():
            lines = env_path.read_text(encoding="utf-8").splitlines(keepends=True)
            token_updated = False

            for i, line in enumerate(lines):
                if line.startswith("AUTH_TOKEN="):
                    lines[i] = token_line
                    token_updated = True
                    break

            if not token_updated:
                lines.append("\n" + token_line)

            env_path.write_text("".join(lines), encoding="utf-8")
        else:
            env_path.write_text(token_line, encoding="utf-8")

        os.environ["AUTH_TOKEN"] = token
