from unittest import TestCase

from src.constant import FLO_CHART_URI, GENIE_CHART_URI, MELON_CHART_URI, VIBE_CHART_URI
from src.music_chart_crawler.music_chart import MusicChart


class MusicChartTest(TestCase):
    def test_should_have_melon_genie_flo_vibe_top_100(self):
        music_chart = MusicChart()

        melon = music_chart.melon
        genie = music_chart.genie
        flo = music_chart.flo
        vibe = music_chart.vibe

        self.assertEqual(melon["uri"], MELON_CHART_URI)
        self.assertEqual(genie["uri"], GENIE_CHART_URI)
        self.assertEqual(flo["uri"], FLO_CHART_URI)
        self.assertEqual(vibe["uri"], VIBE_CHART_URI)

        self.assertEqual(len(melon["chart"]), 100)
        self.assertEqual(len(genie["chart"]), 100)
        self.assertEqual(len(flo["chart"]), 100)
        self.assertEqual(len(vibe["chart"]), 100)
