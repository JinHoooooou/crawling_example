import requests
from bs4 import BeautifulSoup

from src.constant import VIBE_CHART_URI, VIBE_CHART_API


class VibeChartCrawler:
    def __init__(self, header, uri=VIBE_CHART_API):
        self._page = requests.get(url=uri, headers=header)
        self._crawler = BeautifulSoup(self._page.text, "xml")

    def get_title(self):
        return self._crawler.select("title")[0].text

    def get_song_info_top_100(self):
        result = {"uri": VIBE_CHART_URI, "chart": []}
        music_chart_top_100 = self._crawler.select("track")
        for track in music_chart_top_100:
            title = track.select("trackTitle")[0].text[9:-3]
            artist = track.select("artistName")[0].text[9:-3]

            info = {"title": title, "artist": artist}
            result["chart"].append(info)

        return result
