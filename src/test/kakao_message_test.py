import json
import os
from unittest import TestCase

import requests

from constant import KAKAO_API_HOST, MESSAGE_TO_ME_URI, CONFIG_DIR, MELON_CHART_URI
from music_chart_crawler.music_chart import MusicChart
from kakao.message import KakaoMessage


class KakaoMessageToMeTest(TestCase):
    def setUp(self) -> None:
        pass

    def test_send_text_message_success(self):
        """"""
        # Given: 요청에 필요한 정보들이 주어진다.
        kakao_message = KakaoMessage()

        response = kakao_message.send_text_message(text="테스트", link="https://naver.com")

        print(response.text)

    def test_should_response_200_on_feed_message_to_me(self):
        # Given: 요청에 필요한 정보들이 주어진다.
        melon_chart = {"uri": MELON_CHART_URI, "chart": "멜론 차트"}
        link = melon_chart["uri"]
        text = melon_chart["chart"]
        feed_template = {
            "object_type": "feed",
            "content": {
                "title": text,
                "description": text,
                "image_url": "https://mud-kage.kakao.com/dn/NTmhS/btqfEUdFAUf/FjKzkZsnoeE4o19klTOVI1/openlink_640x640s.jpg",
                "image_width": 640,
                "image_height": 640,
                "link": {
                    "web_url": link,
                    "mobile_web_url": link,
                    "android_execution_params": "contentId=100",
                    "ios_execution_params": "contentId=100"
                }
            },
        }
        data = {"template_object": json.dumps(feed_template)}

        # When: 나에게 메시지 보내기 요청
        response = requests.post(self._request_url, data=data, headers=self._headers)

        # Then: 응답의 status code는 200이어야 한다.
        self.assertEqual(response.status_code, 200)
        # And: 응답의 result_code는 0이다.
        response_body = json.loads(response.text)
        self.assertEqual(response_body["result_code"], 0)

    def test_should_response_200_location_messsage_to_me(self):
        # Given: 요청에 필요한 정보들이 주어진다.
        melon_chart = {"uri": MELON_CHART_URI, "chart": "멜론 차트"}
        link = melon_chart["uri"]
        text = melon_chart["chart"]
        feed_template = {
            "object_type": "location",
            "content": {
                "title": text,
                "description": text,
                "image_url": "https://mud-kage.kakao.com/dn/NTmhS/btqfEUdFAUf/FjKzkZsnoeE4o19klTOVI1/openlink_640x640s.jpg",
                "image_width": 640,
                "image_height": 640,
                "link": {
                    "web_url": link,
                    "mobile_web_url": link,
                    "android_execution_params": "platform=android",
                    "ios_execution_params": "platform=ios"
                }
            },
            "address": text
        }
        data = {"template_object": json.dumps(feed_template)}

        # When: 나에게 메시지 보내기 요청
        response = requests.post(self._request_url, data=data, headers=self._headers)

        # Then: 응답의 status code는 200이어야 한다.
        self.assertEqual(response.status_code, 200)
        # And: 응답의 result_code는 0이다.
        response_body = json.loads(response.text)
        self.assertEqual(response_body["result_code"], 0)

    def _get_access_token(self):
        with open(os.path.join(CONFIG_DIR, "access_data.json")) as json_file:
            return json.load(json_file)["access_token"]

    def _get_melon_top_100(self):
        music_chart = MusicChart()
        return music_chart.melon

    def _formatting_text(self, chart):
        result = "멜론\n"
        for index, track in enumerate(chart):
            result += f"{index + 1}. {track[1]} - {track[0]}\n"

        print(result.strip())
        return result
