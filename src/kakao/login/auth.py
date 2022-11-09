import json
import os

import requests

from constant import CONFIG_DIR, KAKAO_REDIRECT_URL_LIST, TOKEN_URI, KAKAO_LOGIN_HOST


def read_rest_api_key():
    with open(os.path.join(CONFIG_DIR, "rest_api_key")) as key_file:
        key = key_file.read()

    return key


def read_auth_code():
    with open(os.path.join(CONFIG_DIR, "auth_code")) as code_file:
        code = code_file.read()

    return code


my_kakao_rest_api_key = read_rest_api_key()
my_kakao_auth_code = read_auth_code()

request_url = f"{KAKAO_LOGIN_HOST}{TOKEN_URI}"
data = {
    "grant_type": "authorization_code",
    "client_id": my_kakao_rest_api_key,
    "redirect_url": KAKAO_REDIRECT_URL_LIST[0],
    "code": my_kakao_auth_code
}

response = requests.post(request_url, data=data)

with open(os.path.join(CONFIG_DIR, "access_data.json"), mode="w") as json_file:
    json_file.write(response.text)
