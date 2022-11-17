import json

import requests
from bs4 import BeautifulSoup

from constant import (
    FLO_ALBUM_DETAIL_URI,
    FLO_CHART_API,
    FLO_CHART_URI,
    GENIE_ALBUM_DETAIL_URI,
    GENIE_CHART_URI,
    MELON_ALBUM_DETAIL_URI,
    MELON_CHART_URI,
    USER_AGENT,
    VIBE_ALBUM_DETAIL_URI,
    VIBE_CHART_API,
    VIBE_CHART_URI,
)


def extract_melon_top_3():
    html_page = requests.get(MELON_CHART_URI, headers=USER_AGENT)
    parser = BeautifulSoup(html_page.text, "lxml")
    top_3 = parser.select("tr.lst50")[:3]

    result = {"url": MELON_CHART_URI, "name": "멜론", "track": []}
    for track in top_3:
        title = track.select("div.wrap_song_info a")[0].text
        artist = track.select("div.wrap_song_info a")[1].text
        album_cover_url = track.select("div.wrap img[src]")[0]["src"]
        album_id = album_cover_url.split("/")[9].split("_")[0]

        result["track"].append(
            {
                "title": title,
                "artist": artist,
                "album_cover_url": album_cover_url,
                "detail": MELON_ALBUM_DETAIL_URI + album_id,
            }
        )

    return result


def extract_genie_top_3():
    html_page = requests.get(GENIE_CHART_URI, headers=USER_AGENT)
    parser = BeautifulSoup(html_page.text, "lxml")

    result = {"url": GENIE_CHART_URI, "name": "지니", "track": []}
    top_3_tr = parser.select("tr.list")[:3]

    for track in top_3_tr:
        title = track.select("a.title")[0].text.strip()
        artist = track.select("a.artist")[0].text.strip()
        album_cover_url = "https://" + track.select("a.cover img")[0]["src"][2:-19]
        album_id = album_cover_url.split("/")[9].split("_")[0]

        result["track"].append(
            {
                "title": title,
                "artist": artist,
                "album_cover_url": album_cover_url,
                "detail": GENIE_ALBUM_DETAIL_URI + album_id,
            }
        )

    return result


def extract_flo_top_3():
    html_page = requests.get(FLO_CHART_API, headers=USER_AGENT)
    parser = json.loads(html_page.text)

    result = {"url": FLO_CHART_URI, "name": "플로", "track": []}
    top_3_tr = parser["data"]["trackList"][:3]
    for track in top_3_tr:
        title = track["name"]
        artist = track["representationArtist"]["name"]
        album_cover_url = track["album"]["imgList"][1]["url"]
        album_id = str(track["album"]["id"])
        parsing = ""
        for digit in album_id:
            if digit == "0":
                parsing += "d"
            elif digit == "1":
                parsing += "a"
            elif digit == "2":
                parsing += "n"
            elif digit == "3":
                parsing += "i"
            elif digit == "4":
                parsing += "e"
            elif digit == "5":
                parsing += "l"
            elif digit == "6":
                parsing += "z"
            elif digit == "7":
                parsing += "o"
            elif digit == "8":
                parsing += "h"
            elif digit == "9":
                parsing += "y"

        result["track"].append(
            {
                "title": title,
                "artist": artist,
                "album_cover_url": album_cover_url,
                "detail": FLO_ALBUM_DETAIL_URI + parsing + "/albumtrack",
            }
        )

    return result


def extract_vibe_top_3():
    html_page = requests.get(VIBE_CHART_API)
    parser = BeautifulSoup(html_page.text, "lxml-xml")

    result = {"url": VIBE_CHART_URI, "name": "바이브", "track": []}
    top_3_tr = parser.select("track")[:3]
    for track in top_3_tr:
        title = track.select("trackTitle")[0].text
        artist = track.select("artistName")[0].text
        album_cover_url = track.select("imageUrl")[0].text
        album_id = album_cover_url.split("/")[6].split(".")[0]

        result["track"].append(
            {
                "title": title,
                "artist": artist,
                "album_cover_url": album_cover_url,
                "detail": VIBE_ALBUM_DETAIL_URI + album_id,
            }
        )

    return result


def extract_music_charts():
    melon_top_3 = extract_melon_top_3()
    genie_top_3 = extract_genie_top_3()
    flo_top_3 = extract_flo_top_3()
    vibe_top_3 = extract_vibe_top_3()

    result = [melon_top_3, genie_top_3, flo_top_3, vibe_top_3]

    return result
