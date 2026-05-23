from TP_Polako_E2E.api.base_api import BaseApi


class ProfileApi(BaseApi):
    def get_profile_data(self) -> dict:
        response = self.session.get(f"{self.base_url}/api/users/me")
        response.raise_for_status()
        return response.json()
