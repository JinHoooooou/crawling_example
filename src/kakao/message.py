import json
import os

import requests

from constant import KAKAO_API_HOST, MESSAGE_TO_ME_URI, CONFIG_DIR, ACCESS_TOKEN_INFO_URI, KAKAO_AUTH_HOST, TOKEN_URI


class KakaoMessage:
    def __init__(self):
        self._kakao_rest_api_key = os.getenv("KAKAO_REST_API_KEY", None)
        self._access_token = None
        self._refresh_token = None
        self._get_env()

    def _get_env(self):
        with open(os.path.join(CONFIG_DIR, ".env"), "r") as env_file:
            env = json.load(env_file)
            self._access_token = env.get("access_token", None)
            self._refresh_token = env.get("refresh_token", None)

    def send_text_message(self, text, link):
        if not self._is_valid_token():
            self._update_token()

        url = KAKAO_API_HOST + MESSAGE_TO_ME_URI
        headers = {"Authorization": f"Bearer {self._access_token}"}
        text_template = {
            "object_type": "text",
            "text": text,
            "link": {
                "web_url": link,
                "mobile_web_url": link
            },
            "button_title": "더보기"
        }
        data = {"template_object": json.dumps(text_template)}

        response = requests.post(url, data=data, headers=headers)

        return response

    def _is_valid_token(self):
        url = KAKAO_API_HOST + ACCESS_TOKEN_INFO_URI
        headers = {"Authorization": f"Bearer {self._access_token}"}

        response = requests.get(url=url, headers=headers)

        return response.status_code == 200

    def _update_token(self):
        url = KAKAO_AUTH_HOST + TOKEN_URI
        data = {
            "grant_type": "refresh_token",
            "client_id": "9bb7b58c60a4a53ab539d3b89e6d6f65",
            "refresh_token": self._refresh_token
        }

        response = requests.post(url=url, data=data)
        response_body = json.loads(response.text)

        with open(os.path.join(CONFIG_DIR, ".env"), "w") as env_file:
            self._access_token = response_body.get("access_token", self._access_token)
            self._refresh_token = response_body.get("access_token", self._refresh_token)
            env_file.write(response.text)
