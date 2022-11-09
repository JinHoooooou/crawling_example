from kakao.message.message import KakaoMessage
from music_chart_crawler.music_chart import MusicChart
from constant import MELON_CHART_URI

if __name__ == '__main__':
    music_chart = MusicChart()
    kakao_message = KakaoMessage()

    kakao_message.send_text_message(text="텍스트", link=MELON_CHART_URI)
