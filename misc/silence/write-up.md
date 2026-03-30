# Category

misc

# Overview

Nothing gets revealed when everything's piped to /dev/null, right?

# Analysis

jail.py에서는 사용자가 10글자 안의 input을 입력하면 정의되어 있는 `cat flag.txt > {input}`input에 위치하여 실행된다. 

하지만 `stdin`, `stdout`, `stderr` 모두 `/dev/null`을 가리키고 있어서 일반적인 출력 방법으로는 flag를 확인할 수가 없다.

# Exploitation

`cat flag.txt`를 통해 읽은 `stdout`를 리다이렉션을 통해 10글자 이내인 `/dev/tty`로 전달하여 사용자 터미널에서 바로 출력이 될 수 있게하면, flag를 획득할 수 있다.

```bash
cat flag.txt > /dev/tty
```

# Flag

`Alpaca{1t...gh}`
