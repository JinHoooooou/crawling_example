# 헤더
import os

USER_AGENT = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

# 크롤링 할 음원 플랫폼 URI
MELON_CHART_URI = "https://www.melon.com/chart/"
MELON_ALBUM_DETAIL_URI = "https://www.melon.com/album/detail.htm?albumid="

GENIE_CHART_URI = "https://www.genie.co.kr/chart/top200"
GENIE_ALBUM_DETAIL_URI = "https://www.genie.co.kr/detail/albumInfo?axnm="

FLO_CHART_URI = "https://www.music-flo.com/browse"
FLO_ALBUM_DETAIL_URI = "https://www.music-flo.com/detail/album/"
FLO_CHART_API = "https://www.music-flo.com/api/display/v1/browser/chart/1/track/list?size=100"

VIBE_CHART_URI = "https://vibe.naver.com/chart/total"
VIBE_ALBUM_DETAIL_URI = "https://vibe.naver.com/album/"
VIBE_CHART_API = "https://apis.naver.com/vibeWeb/musicapiweb/vibe/v1/chart/track/total?start=1&display=100"

# 카카오 API URI
KAKAO_AUTH_HOST = "https://kauth.kakao.com"
TOKEN_URI = "/oauth/token"

KAKAO_API_HOST = "https://kapi.kakao.com"
MESSAGE_TO_ME_URI = "/v2/api/talk/memo/default/send"
ACCESS_TOKEN_INFO_URI = "/v1/user/access_token_info"

# directory path
PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_DIR = os.path.join(PROJECT_ROOT_DIR, "config")
