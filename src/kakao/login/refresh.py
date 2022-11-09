import json
import os

import requests

from constant import KAKAO_LOGIN_HOST, TOKEN_URI, CONFIG_DIR


def read_rest_api_key():
    with open(os.path.join(CONFIG_DIR, "rest_api_key")) as key_file:
        key = key_file.read()

    return key


def read_access_data():
    with open(os.path.join(CONFIG_DIR, "access_data.json"), mode="r") as json_file:
        access_data = json.load(json_file)

    return access_data


my_kakao_rest_api_key = read_rest_api_key()
my_kakao_access_data = read_access_data()
print(my_kakao_access_data)
request_url = f"{KAKAO_LOGIN_HOST}{TOKEN_URI}"
data = {
    "grant_type": "refresh_token",
    "client_id": my_kakao_rest_api_key,
    "refresh_token": my_kakao_access_data["refresh_token"],
}

response = requests.post(request_url, data=data)

new_kakao_access_data = json.loads(response.text)

my_kakao_access_data["access_token"] = new_kakao_access_data["access_token"]
my_kakao_access_data["refresh_token"] = new_kakao_access_data.get("refresh_token",
                                                                  my_kakao_access_data["refresh_token"])
my_kakao_access_data["refresh_token_expires_in"] = new_kakao_access_data.get("refresh_token_expires_in",
                                                                             my_kakao_access_data[
                                                                                 "refresh_token_expires_in"])
my_kakao_access_data["expires_in"] = new_kakao_access_data["expires_in"]

with open(os.path.join(CONFIG_DIR, "access_data.json"), mode="w") as json_file:
    json_file.write(json.dumps(my_kakao_access_data))
