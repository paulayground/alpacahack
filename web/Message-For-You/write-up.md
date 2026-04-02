# Category

web

# Overview

Please find my hidden message.

# Analysis

`GET /`에 접속할 때마다 session이 쿠키에 심어져 발급되며, flask는 세션을 생성할 때 `Payload.Timestamp.Signature`로 구분하여 base64 인코딩하여 반환한다.

브라우저 `Application`에서 session에 대한 값인 `.eJw...S59.ac46DA.ceS...2CM`를 획득할 수 있다.

서명을 했기 때문에 키 노출이 아니라면 변조가 되진 않지만 base64 디코딩을 통한 데이터의 값은 노출될 수 있다.

# Exploitation

세션에 저장되는 데이터의 용량이 크기 때문에 flask에서는 `zlib` 통해 압축하고 base64 인코딩을 수행한다.

그렇기 때문에 payload 부분인 `.eJw...S59`와 같이 앞에 `.`이 붙는 것을 확인할 수 있다.

`zlib` 압축을 해제하고 url safe base64 디코딩을 하면 flag를 획득 할 수 있다.

```py
# solve.py

# GET / 요청
res = req(
    url="http://34.170.146.252:53703",
    method="GET",
)

session = res.cookies["session"]

# payload 부분 추출
session_header = "." + session.split(".")[1]

# 생성될 때 버려졌던 패딩문자를 "===" 채움
# base65 url safe 디코딩
decoded = base64.urlsafe_b64decode(session_header + "===")
data = zlib.decompress(decoded).decode("utf-8")

matched = re.search("Alpaca\\{.*?\\}", data)
print(matched.group() if matched else "NO FLAG")
```

# Flag

`Alpaca{Co...0u}`
