import json
import os

import requests

from constant import KAKAO_API_HOST, ACCESS_TOKEN_INFO_URI, KAKAO_AUTH_HOST, TOKEN_URI, CONFIG_DIR


def is_valid(token):
    url = KAKAO_API_HOST + ACCESS_TOKEN_INFO_URI
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url=url, headers=headers)

    return response.status_code == 200


def renew_tokens():
    url = KAKAO_AUTH_HOST + TOKEN_URI
    client_id = os.getenv("KAKAO_REST_API_KEY", None)
    refresh_token = os.getenv("KAKAO_REFRESH_TOKEN", None)

    if client_id is None:
        print("Invalid Client ID, Check Your Client ID", flush=True)
        return None, None
    if refresh_token is None:
        print("Invalid Refresh Token, Update Tokens Using Authorization Code", flush=True)
        return None, None

    data = {
        "grant_type": "refresh_token",
        "client_id": client_id,
        "refresh_token": refresh_token
    }

    response = requests.post(url=url, data=data)
    if response.status_code != 200:
        print("Invalid Refresh Token, Update Tokens Using Authorization Code", flush=True)
        return None, None

    response_body = json.loads(response.text)
    updated_access_token = response_body.get("access_token", None)
    updated_refresh_token = response_body.get("refresh_token", refresh_token)

    return updated_access_token, updated_refresh_token


def get_tokens():
    access_token = os.getenv("KAKAO_ACCESS_TOKEN", None)
    refresh_token = os.getenv("KAKAO_REFRESH_TOKEN", None)

    if not is_valid(access_token):
        access_token, refresh_token = renew_tokens()

    return f"{access_token} {refresh_token}"


if __name__ == "__main__":
    print(get_tokens())
