# Category

misc

# Overview

Can you show a file which has a strange filename?

# Analysis

- 서버에 접속한 결과 제시된 코드와 같이 `ls`가 실행되며 현재 파일 리스트가 보여진다.

  ```sh
  $ls
  -
  server.py
  ```

  `-` 라는 파일이 존재하는 것을 알 수 있으며, `-` 문자는 명령에 붙는 옵션으로 사용되기 때문에, `cat`을 사용하서 파일의 읽는 경우 `cat -` 과 같이 옵션처럼 해석되어 그냥 `-`를 사용해서 읽을 경우 읽을 수 없다.

- 문제를 통해 `-` 파일이 flag파일 이라는 것을 확인할 수 있다.

# Exploitation

파일 이름으로써 읽기위해 `./-` 와 같이 경로 표시를 하여 읽으면 flag를 획득할 수 있다.

```sh
$ cat ./-
Alpaca{It...us}
```

# Flag

`Alpaca{It...us}`
