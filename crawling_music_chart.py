import json

import requests
from bs4 import BeautifulSoup

from constant import MELON_CHART_URI, USER_AGENT, GENIE_CHART_URI, FLO_CHART_API, FLO_CHART_URI, VIBE_CHART_API, \
    VIBE_CHART_URI


def extract_melon_top_3():
    html_page = requests.get(MELON_CHART_URI, headers=USER_AGENT)
    parser = BeautifulSoup(html_page.text, "lxml")

    result = {"url": MELON_CHART_URI, "name": "멜론", "track": []}
    top_3_tr = parser.select("tr.lst50")[:3]
    for track in top_3_tr:
        title = track.select("div.wrap_song_info a")[0].text
        artist = track.select("div.wrap_song_info a")[1].text

        result["track"].append((title, artist))

    return result


def extract_genie_top_3():
    html_page = requests.get(GENIE_CHART_URI, headers=USER_AGENT)
    parser = BeautifulSoup(html_page.text, "lxml")

    result = {"url": GENIE_CHART_URI, "name": "지니", "track": []}
    top_3_tr = parser.select("tr.list")[:3]

    for track in top_3_tr:
        title = track.select("a.title")[0].text.strip()
        artist = track.select("a.artist")[0].text.strip()

        result["track"].append((title, artist))

    return result


def extract_flo_top_3():
    html_page = requests.get(FLO_CHART_API, headers=USER_AGENT)
    parser = json.loads(html_page.text)

    result = {"url": FLO_CHART_URI, "name": "플로", "track": []}
    top_3_tr = parser["data"]["trackList"][:3]
    for track in top_3_tr:
        title = track["name"]
        artist = track["representationArtist"]["name"]

        result["track"].append((title, artist))

    return result


def extract_vibe_top_3():
    html_page = requests.get(VIBE_CHART_API)
    parser = BeautifulSoup(html_page.text, "lxml-xml")

    result = {"url": VIBE_CHART_URI, "name": "바이브", "track": []}
    top_3_tr = parser.select("track")[:3]
    for track in top_3_tr:
        title = track.select("trackTitle")[0].text
        artist = track.select("artistName")[0].text

        result["track"].append((title, artist))

    return result


def extract_music_charts():
    melon_top_3 = extract_melon_top_3()
    genie_top_3 = extract_genie_top_3()
    flo_top_3 = extract_flo_top_3()
    vibe_top_3 = extract_vibe_top_3()

    result = [melon_top_3, genie_top_3, flo_top_3, vibe_top_3]

    return result
