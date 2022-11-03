import json
from unittest import TestCase

from src.constant import USER_AGENT, MELON_CHART_URI, GENIE_CHART_URI
from src.music_chart_crawler.genie import GenieChartCrawler
from src.music_chart_crawler.melon import MelonChartCrawler


class MelonChartPageCrawlingTest(TestCase):
    def setUp(self) -> None:
        self._uri = MELON_CHART_URI
        self._header = {"User-Agent": USER_AGENT}

    def test_should_return_page_title_on_get_title_method(self):
        # Given: 음원 차트 크롤러가 주어진다.
        crawler = MelonChartCrawler(uri=self._uri, header=self._header)

        # When: get_title() 메소드를 호출 할 때
        title = crawler.get_title()

        # Then: "멜론차트"가 포함되어야 한다.
        self.assertIn("멜론차트", title)

    def test_should_return_json_format_music_chart_and_page_uri(self):
        # Given: 음원 차트 크롤러가 주어진다.
        crawler = MelonChartCrawler(uri=self._uri, header=self._header)

        # When: get_song_info_top_100() 메소드를 호출 할 때
        top_100_chart = crawler.get_song_info_top_100()

        # Then: top 100 차트와 page uri를 json형태로 리턴해야 한다.
        self.assertTrue("uri" in top_100_chart)
        self.assertTrue("chart" in top_100_chart)
        self.assertTrue(len(top_100_chart["chart"]), 100)


class GenieChartPageCrawlingTest(TestCase):
    def setUp(self) -> None:
        self._uri = GENIE_CHART_URI
        self._header = {"User-Agent": USER_AGENT}

    def test_should_return_page_title_on_get_title_method(self):
        # Given: 음원 차트 크롤러가 주어진다.
        crawler = GenieChartCrawler(uri=self._uri, header=self._header)

        # When: get_title() 메소드를 호출 할 때
        title = crawler.get_title()

        # Then: "지니차트"가 포함되어야 한다.
        self.assertIn("지니차트", title)

    def test_should_return_json_format_music_chart_and_page_uri(self):
        # Given: 음원 차트 크롤러가 주어진다.
        crawler = GenieChartCrawler(uri=self._uri, header=self._header)

        # When: get_song_info_top_100() 메소드를 호출 할 때
        top_100_chart = crawler.get_song_info_top_100()

        # Then: top 100 차트와 page uri를 json형태로 리턴해야 한다.
        self.assertTrue("uri" in top_100_chart)
        self.assertTrue("chart" in top_100_chart)
        self.assertTrue(len(top_100_chart["chart"]), 100)
