import time

from kakao.message import KakaoMessage
from music_chart_crawler.music_chart import MusicChart
import schedule


def format_message(chart, platform):
    result = f"{platform}\n"
    for index, track in enumerate(chart):
        result += f"{index + 1}. {track[1]} - {track[0]}\n"

    return result.strip()


def send_message():
    chart = MusicChart()
    kakao_message = KakaoMessage()

    chart_list = [(chart.melon, "멜론"), (chart.genie, "지니"), (chart.flo, "플로"), (chart.vibe, "바이브")]
    for platform in chart_list:
        track_list = format_message(platform[0]["chart"], platform[1])
        url = platform[0]["uri"]
        kakao_message.send_text_message(text=track_list, link=url)


if __name__ == '__main__':
    schedule.every().hour.at(":00").do(send_message)
    while True:
        schedule.run_pending()
        time.sleep(1)
