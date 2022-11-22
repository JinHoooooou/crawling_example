import os

import requests

from constant import KAKAO_AUTH_HOST, TOKEN_URI, CONFIG_DIR

url = KAKAO_AUTH_HOST + TOKEN_URI
data = {
    "grant_type": "authorization_code",
    "client_id": os.getenv("KAKAO_REST_API_KEY", None),
    "redirect_uri": "https://naver.com",
    "code": ""
}

response = requests.post(url, data=data)

if response.status_code == 200:
    with open(os.path.join(CONFIG_DIR, ".env"), "w") as env:
        env.write(response.text)
