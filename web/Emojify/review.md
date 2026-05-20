# // 로 시작하는 URL Protocol-relative URL

브라우저에 로드된 페이지의 Protocol을 따라감

그래서 https:// 서비스에서 열었다면 https://로 연결하고, http://에서 열었다면 http://로 연결된다.

# const url = new URL(url [, base])

url이 입력값이 //로 시작하는 거처럼 절대경로를 가지면, 파서는 경로가 아니라 URL 형태로 인식한다.

base URL에서 프로토콜(http:) 정보만 추출한 뒤, 나머지 호스트와 경로는 첫 번째 인자의 데이터로 통째로 덮어씌워 버린다.
