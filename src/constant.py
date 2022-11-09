import os

USER_AGENT = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

MELON_CHART_URI = "https://www.melon.com/chart/"
GENIE_CHART_URI = "https://www.genie.co.kr/chart/top200"
FLO_CHART_URI = "https://www.music-flo.com/browse"
FLO_CHART_API = "https://www.music-flo.com/api/display/v1/browser/chart/1/track/list?size=100"
VIBE_CHART_URI = "https://vibe.naver.com/chart/total"
VIBE_CHART_API = "https://apis.naver.com/vibeWeb/musicapiweb/vibe/v1/chart/track/total?start=1&display=100"

PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_DIR = os.path.join(PROJECT_ROOT_DIR, "config")

KAKAO_LOGIN_HOST = "https://kauth.kakao.com"
TOKEN_URI = "/oauth/token"

KAKAO_MESSAGE_HOST = "https://kapi.kakao.com"
KAKAO_MESSAGE_TO_ME_URI = "/v2/api/talk/memo/default/send"

KAKAO_REDIRECT_URL_LIST = [
    "https://naver.com",
    "https://melon.com"
    "https://google.com"
]
