# Category

crypto

# Overview

Hey, friend!

# Analysis

255이하 숫자의 키를 기반으로 연산된다.

# Exploitation

`secrets.randbelow(256)`를 통해 0~255 숫자로 이루어진 키라는 단서가 있다. 키를 바꿔가면서 올바른 flag를 구할 때까지 brute force 방법을 수행할 수 있다.

```py
# solve.py

key = 0
while key < 256:
    key += 1

    # cts길이와 같은 리스트 생성
    ct = [0] * len(cts)

    # ct 첫번째를 키와 XOR연산 하여 역산
    ct[0] = cts[0] ^ key
    # 나머지 원본 코드와 동일한 방식으로 역산
    for i in range(1, len(cts)):
        ct[i] = cts[i] ^ ct[i - 1]

    # rot13으로 복호화
    flag = rot13("".join(chr(c) for c in ct))

    if "Alpaca" in flag:
        print("key -> ", key)
        print(flag)
        break
```

# Flag

`Alpaca{Pl...re}`
