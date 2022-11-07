import json

import requests
from bs4 import BeautifulSoup

from src.constant import MELON_CHART_URI, USER_AGENT, GENIE_CHART_URI, FLO_CHART_API, FLO_CHART_URI, VIBE_CHART_URI, \
    VIBE_CHART_API


class MusicChart:
    def __init__(self):
        self.melon = self._get_melon_top_100()
        self.genie = self._get_genie_top_100()
        self.flo = self._get_flo_top_100()
        self.vibe = self._get_vibe_top_100()

    def _get_melon_top_100(self):
        html_page = requests.get(MELON_CHART_URI, headers=USER_AGENT)
        parser = BeautifulSoup(html_page.text, "lxml")

        result = {"uri": MELON_CHART_URI, "chart": []}
        table = parser.find_all("tr", attrs={"class": ["lst50", "lst100"]})
        for track in table:
            title = track.select("div.wrap_song_info a")[0].text
            artist = track.select("div.wrap_song_info a")[1].text

            result["chart"].append((title, artist))

        return result

    def _get_genie_top_100(self):
        table = []
        for index in range(1, 3):
            html_page = requests.get(GENIE_CHART_URI, headers=USER_AGENT, params={"pg": index})
            parser = BeautifulSoup(html_page.text, "lxml")
            table += parser.find_all("tr", attrs={"class": "list"})

        result = {"uri": GENIE_CHART_URI, "chart": []}
        for track in table:
            title = track.select("a.title")[0].text.strip()
            artist = track.select("a.artist")[0].text.strip()

            result["chart"].append((title, artist))

        return result

    def _get_flo_top_100(self):
        html_page = requests.get(FLO_CHART_API)
        parser = json.loads(html_page.text)

        result = {"uri": FLO_CHART_URI, "chart": []}
        table = parser["data"]["trackList"]
        for track in table:
            title = track["name"]
            artist = track["representationArtist"]["name"]

            result["chart"].append((title, artist))

        return result

    def _get_vibe_top_100(self):
        html_page = requests.get(VIBE_CHART_API)
        parser = BeautifulSoup(html_page.text, "lxml-xml")

        result = {"uri": VIBE_CHART_URI, "chart": []}
        table = parser.select("track")
        for track in table:
            title = track.select("trackTitle")[0].text
            artist = track.select("artistName")[0].text

            result["chart"].append((title, artist))

        return result
