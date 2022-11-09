import json
import os

import requests

from constant import KAKAO_MESSAGE_HOST, KAKAO_MESSAGE_TO_ME_URI, CONFIG_DIR


class KakaoMessage:
    def __init__(self):
        self._request_url = f"{KAKAO_MESSAGE_HOST}{KAKAO_MESSAGE_TO_ME_URI}"
        self._headers = {"Authorization": f"Bearer {self._get_access_token()}"}

    def _get_access_token(self):
        with open(os.path.join(CONFIG_DIR, "access_data.json")) as json_file:
            return json.load(json_file)["access_token"]

    def send_text_message(self, text, link):
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

        response = requests.post(self._request_url, data=data, headers=self._headers)

        return response
