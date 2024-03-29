from crawling_music_chart import extract_music_charts
from kakao_message import send_list_message_to_me

if __name__ == "__main__":
    charts_by_platform = extract_music_charts()
    response_list = []

    for platform in charts_by_platform:
        top3_track = platform.get("track")
        url = platform.get("url")
        name = platform.get("name")

        response_list.append(send_list_message_to_me(top3_track, name, url))

    print(response_list)