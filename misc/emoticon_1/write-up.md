# Category

misc

# Overview

One character only.

# Analysis

- 한 글자만 입력하여 flag를 확인해야하며, `source`명령어를 통해 쉘스크립트 읽듯이 실행하지만 스크립트 문법과 달라 실패하고, 그 에러가 쉘에 출력되는 방법으로 flag를 확인할 수 있다.

- `source` 명령어는 `.`로 대신하여 쓸 수 있다.

# Exploitation

입력값이 내부적으로 `/app/flag.txt`와 결합되어 실행되는 구조이기 때문에, `.`을 입력하면 `. /app/flag.txt` 형태가 되어 `source`가 실행된다.

```bash
$ > .
sh: 1: /app/flag.txt: Alpaca{bu...in}: not found
```

# Flag

`Alpaca{bu...in}`
