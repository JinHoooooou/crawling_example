import json
import os

import requests

from constant import KAKAO_API_HOST, KAKAO_AUTH_HOST, MESSAGE_TO_ME_URI, TOKEN_URI


def get_access_token():
    url = KAKAO_AUTH_HOST + TOKEN_URI
    data = {
        "grant_type": "refresh_token",
        "client_id": os.getenv("KAKAO_REST_API_KEY"),
        "refresh_token": os.getenv("KAKAO_REFRESH_TOKEN", None),
    }

    response = requests.post(url=url, data=data)
    response_body = json.loads(response.text)

    return response_body.get("access_token", None)


def build_list_template(data, platform_name, link):
    list_template = {
        "object_type": "list",
        "header_title": f"{platform_name} 차트",
        "header_link": {
            "web_url": link,
            "mobile_web_url": link,
        },
        "contents": [
            {
                "title": chart["title"],
                "description": chart["artist"],
                "image_url": chart["album_cover_url"],
                "image_width": 640,
                "image_height": 640,
                "link": {
                    "web_url": chart["detail"],
                    "mobile_web_url": chart["detail"],
                },
            }
            for chart in data
        ],
        "button_title": "더보기",
    }

    return list_template


def send_list_message_to_me(data, platform_name, link):
    access_token = get_access_token()

    url = KAKAO_API_HOST + MESSAGE_TO_ME_URI
    headers = {"Authorization": f"Bearer {access_token}"}
    list_template = build_list_template(data, platform_name, link)
    data = {"template_object": json.dumps(list_template, ensure_ascii=False)}

    response = requests.post(url, data=data, headers=headers)

    return response
