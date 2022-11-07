import json

import requests

from src.constant import FLO_CHART_URI


class FloChartCrawler:
    def __init__(self, header, uri=FLO_CHART_URI):
        self._page = requests.get(url=uri, headers=header)
        self._crawler = json.loads(self._page.text)

    def get_title(self):
        return self._crawler["data"]["name"]

    def get_song_info_top_100(self):
        result = {"uri": FLO_CHART_URI, "chart": []}
        music_chart_top_100 = self._crawler["data"]["trackList"]

        for track in music_chart_top_100:
            title = track["name"]
            artist = track["representationArtist"]["name"]

            info = {"title": title, "artist": artist}
            result["chart"].append(info)

        return result
