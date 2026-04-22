# 배운 점

`php_admin_flag engine off`: php파일이 실행되는 것을 막는다

# 풀이 과정 기록

도커파일 보니까 플래그 이름이 `flag-[a-zA-Z0-9].txt` 형식이고
이거는 `/flag-*.txt`로 가져오면될 거 같음

`uploads.conf` 보니까 `/var/www/uploads`경로에
`php_admin_flag engine off` 로 `php` 파일을 올려서 실행시킬 수 없다

상대경로로 꺾어서 업로드 시킬 수 있을 것 같음

로컬에서 테스트하며 `/var/www/html` 여기까지 넣은 것을 확인했다.

# 익스플로잇 코드 정리

# 심화 학습 (Deep Dive)

# 참고
