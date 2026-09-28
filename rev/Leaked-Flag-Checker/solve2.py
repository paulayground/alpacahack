# pwn을 사용한 방법

from pwn import *
import string

# 로그 출력 최소화
context.log_level = 'error'

def run_challenge(payload):
    p = process('./attachments/challenge')
    p.sendlineafter(b'Enter flag: ', payload.encode())
    output = p.recvall().decode()
    return output

# 1. 길이 구하기
flag_len = 0
for i in range(1, 32):
    res = run_challenge("A" * i)
    if "Wrong length" not in res:
        flag_len = i
        break

print(f"[+] Flag length: {flag_len}")

# 2. 한 글자씩 맞추기
charset = string.printable.strip() # ascii_letters + digits + punctuation
flag = list("A" * flag_len)

for i in range(flag_len):
    for c in charset:
        flag[i] = c
        res = run_challenge("".join(flag))
        
        # 'Wrong at index i'가 없으면 i번째 문자 맞춤 성공
        if f"Wrong at index {i}" not in res:
            print(f"[+] Found index {i}: {c} -> {''.join(flag)}")
            break

print(f"[★] FLAG: {''.join(flag)}")