import time

import requests
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from src.constant import FLO_CHART_URI
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class FloChartCrawler:
    def __init__(self, header, uri=FLO_CHART_URI):
        self._page = self._get_flo_top_100_html(uri)
        self._crawler = BeautifulSoup(self._page, "lxml")

    def _get_flo_top_100_html(self, uri):
        chrome_driver_options = webdriver.ChromeOptions()
        chrome_driver_options.add_argument("--headless")
        chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                         options=chrome_driver_options)
        chrome_driver.get(uri)
        time.sleep(0.1)
        chrome_driver.find_element(By.CSS_SELECTOR, "button.btn_list_more").send_keys(Keys.ENTER)
        return chrome_driver.page_source

    def get_title(self):
        return self._crawler.select("meta[property*=title]")[0]["content"]

    def get_song_info_top_100(self):
        result = {"uri": FLO_CHART_URI, "chart": []}
        music_chart_top_100 = self._crawler.select("tbody>tr")

        for chart in music_chart_top_100:
            title = chart.select("p.tit")[0].text.strip()
            artist = chart.select("a.last")[0].text.strip()

            info = {"title": title, "artist": artist}
            result["chart"].append(info)

        return result
