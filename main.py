
from crawling_music_chart import extract_music_charts
from kakao_message import send_text_message_to_me


def format_message(chart, platform_name):
    result = f"{platform_name}\n"
    for index, track in enumerate(chart):
        result += f"{index + 1}. {track[1]} - {track[0]}\n"

    return result.strip()


if __name__ == '__main__':
    charts_by_platform = extract_music_charts()

    for platform in charts_by_platform:
        top3_track = platform.get("track")
        url = platform.get("url")
        name = platform.get("name")
        text = format_message(top3_track, name)

        send_text_message_to_me(text=text, link=url)
