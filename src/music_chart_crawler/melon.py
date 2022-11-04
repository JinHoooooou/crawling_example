import requests
from bs4 import BeautifulSoup

from src.constant import MELON_CHART_URI


class MelonChartCrawler:
    def __init__(self, header, uri=MELON_CHART_URI):
        self._page = requests.get(uri, headers=header)
        self._crawler = BeautifulSoup(self._page.text, "lxml")

    def get_title(self):
        return self._crawler.select("title")[0].text

    def get_song_info_top_100(self):
        result = {"uri": self._page.url, "chart": []}
        music_chart_top_100 = self._crawler.find_all("tr", attrs={"class": ["lst50", "lst100"]})
        for chart in music_chart_top_100:
            song_info = chart.select("div.wrap_song_info a")
            info = {"title": song_info[0].text, "singer": song_info[1].text}
            result["chart"].append(info)

        return result
