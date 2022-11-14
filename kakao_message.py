import json
import os

import requests

from constant import KAKAO_API_HOST, MESSAGE_TO_ME_URI, KAKAO_AUTH_HOST, TOKEN_URI


def get_access_token():
    url = KAKAO_AUTH_HOST + TOKEN_URI
    data = {
        "grant_type": "refresh_token",
        "client_id": "9bb7b58c60a4a53ab539d3b89e6d6f65",
        "refresh_token": os.getenv("KAKAO_REFRESH_TOKEN", None)
    }

    response = requests.post(url=url, data=data)
    response_body = json.loads(response.text)

    return response_body.get("access_token", None)


def send_text_message_to_me(text, link):
    access_token = get_access_token()

    url = KAKAO_API_HOST + MESSAGE_TO_ME_URI
    headers = {"Authorization": f"Bearer {access_token}"}
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
