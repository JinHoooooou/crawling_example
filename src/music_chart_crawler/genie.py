import requests
from bs4 import BeautifulSoup

from src.constant import GENIE_CHART_URI


class GenieChartCrawler:
    def __init__(self, header, uri=GENIE_CHART_URI):
        self._pages = [requests.get(url, headers=header) for url in (f"{uri}?pg=1", f"{uri}?pg=2")]
        self._crawlers = [BeautifulSoup(page.text, "lxml") for page in self._pages]

    def get_title(self):
        return self._crawlers[0].select("meta[property*=title]")[0]["content"]

    def get_song_info_top_100(self):
        result = {"uri": self._pages[0].url, "chart": []}
        music_chart_1_to_50 = self._crawlers[0].find_all("tr", attrs={"class": "list"})
        music_chart_51_to_100 = self._crawlers[1].find_all("tr", attrs={"class": "list"})

        music_chart_top_100 = music_chart_1_to_50 + music_chart_51_to_100

        for chart in music_chart_top_100:
            title = chart.select("a.title")[0].text.strip()
            artist = chart.select("a.artist")[0].text

            info = {"title": title, "artist": artist}
            result["chart"].append(info)

        return result
