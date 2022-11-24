import json
import os

import requests

from constant import KAKAO_API_HOST, MESSAGE_TO_ME_URI


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
    access_token = os.getenv("KAKAO_ACCESS_TOKEN", None)

    url = KAKAO_API_HOST + MESSAGE_TO_ME_URI
    headers = {"Authorization": f"Bearer {access_token}"}
    list_template = build_list_template(data, platform_name, link)
    data = {"template_object": json.dumps(list_template, ensure_ascii=False)}

    response = requests.post(url, data=data, headers=headers)

    return response
