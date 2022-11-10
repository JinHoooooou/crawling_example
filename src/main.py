from kakao.message import KakaoMessage
from music_chart_crawler.music_chart import MusicChart
from constant import MELON_CHART_URI


def format_message(chart, platform):
    result = f"{platform}\n"
    for index, track in enumerate(chart):
        result += f"{index + 1}. {track[1]} - {track[0]}\n"

    return result.strip()


if __name__ == '__main__':
    music_chart = MusicChart()
    melon_chart = music_chart.melon
    chart = format_message(melon_chart["chart"], "멜론")
    uri = melon_chart["uri"]

    kakao_message = KakaoMessage()


    kakao_message.send_text_message(text=chart, link=melon_chart["uri"])
