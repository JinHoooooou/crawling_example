import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from src.constant import VIBE_CHART_URI


class VibeChartCrawler:
    def __init__(self, header, uri=VIBE_CHART_URI):
        self._page = self._get_vibe_top_100_html(uri)
        self._crawler = BeautifulSoup(self._page, "lxml")

    def _get_vibe_top_100_html(self, uri):
        chrome_driver_options = webdriver.ChromeOptions()
        chrome_driver_options.add_argument("--headless")
        chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                         options=chrome_driver_options)
        chrome_driver.get(uri)
        time.sleep(0.1)
        return chrome_driver.page_source

    def get_title(self):
        return self._crawler.select("title")[0].text

    def get_song_info_top_100(self):
        result = {"uri": VIBE_CHART_URI, "chart": []}
        music_chart_top_100 = self._crawler.select("tbody>tr")
        for chart in music_chart_top_100:
            title = chart.select("td.song>div.title_badge_wrap")[0].text
            artist = chart.select("td.song>div.artist_sub")[0]["title"]

            info = {"title": title, "artist": artist}
            result["chart"].append(info)

        return result
