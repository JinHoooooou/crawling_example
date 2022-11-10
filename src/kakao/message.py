import json
import os

import requests

from constant import KAKAO_API_HOST, MESSAGE_TO_ME_URI, CONFIG_DIR, ACCESS_TOKEN_INFO_URI, KAKAO_AUTH_HOST, TOKEN_URI


class KakaoMessage:
    def __init__(self):
        self._kakao_rest_api_key = os.getenv("KAKAO_REST_API_KEY", None)
        self._access_token = os.getenv("KAKAO_ACCESS_TOKEN", None)
        self._refresh_token = os.getenv("KAKAO_REFRESH_TOKEN", None)

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
            "button_title": "멜론으로 이동"
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

        os.putenv("KAKAO_ACCESS_TOKEN", response_body["access_token"])
        self._access_token = response_body["access_token"]
        if "refresh_token" in response_body:
            os.putenv("KAKAO_REFRESH_TOKEN", response_body["refresh_token"])
            self._refresh_token = response_body["refresh_token"]
