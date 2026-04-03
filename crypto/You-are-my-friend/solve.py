import ast
from typing import List
from attachments.prob import rot13


with open("./attachments/output.txt") as f:
    output = f.read()

cts: List[int] = ast.literal_eval(output)

for key in range(256):
    ct = [cts[0] ^ key]
    # 나머지 원본 코드와 동일한 방식으로 역산
    for i in range(1, len(cts)):
        ct.append(cts[i] ^ ct[i - 1])

    # rot13으로 복호화
    flag = rot13("".join(chr(c) for c in ct))

    if "Alpaca" in flag:
        print("key -> ", key)
        print(flag)
        break
