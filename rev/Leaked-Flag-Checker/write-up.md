# Category

rev

# Overview

flag checker everyone loves

# Analysis

- `char input`에 길이는 32바이트, 사용자의 입력값의 최대 길이는 1~31바이트가 되는 것을 알 수 있다.

  ```c
  char input[32];
  ...
  scanf("%31s", input);
  ```

- 사용자의 입력값의 각각의 인덱스 값과 7을 xor한 결과를 `xor_flag`값과 비교하여 일치 여부를 판단한다.

  ```c
  for(size_t i = 0; i < flag_len; i++) {
      if((input[i] ^ 7) != xor_flag[i]) {
          printf("Wrong at index %zu\n", i);
          return 1;
      }
  }
  ```

# Exploitation

- 프로그램의 별도의 리버싱을 진행하지 않고 자동화된 코드를 통해 flag를 찾아보았다.

- 코드를 통해 최대 길이를 알 수 있고, 이를 통해 flag의 길이를 `Wrong length` 출력 문구와 비교하여 알아낼 수 있다.

  ```py
  def find_flag_len():
      for i in range(32):
          input = "".join(["0"] * i) + "\n"
          process = subprocess.Popen(
              ["./attachments/challenge"],
              stdin=subprocess.PIPE,
              stdout=subprocess.PIPE,
              stderr=subprocess.PIPE,
              text=True,
              encoding="utf-8",
          )
          stdout_data, stderr_data = process.communicate(input=input)
          if stderr_data:
              print("ERROR -> ", stderr_data)
              raise ValueError
          if "Wrong length" in stdout_data:
              continue
          return i
  ```

- 알아낸 flag의 길이에 맞춰 ascii문자를 반복하여 대입하게되면 `Wrong index`의 일치 여부를 확인하여 해당 인덱스에 올바른 글자를 유추할 수 있다.

  ```py
  def find_flag(flag_len: int):
      candidate = ["0"] * flag_len

      charset = string.digits + string.ascii_letters + string.punctuation

      for can in range(len(candidate)):
          for c in charset:
              candidate[can] = c
              input = "".join(candidate) + "\n"

              process = subprocess.Popen(
                  ["./attachments/challenge"],
                  stdin=subprocess.PIPE,
                  stdout=subprocess.PIPE,
                  stderr=subprocess.PIPE,
                  text=True,
                  encoding="utf-8",
              )
              stdout_data, stderr_data = process.communicate(input=input)
              if stderr_data:
                  print("ERROR -> ", stderr_data)
                  raise ValueError

              output = stdout_data.strip()
              print(input.strip())
              if str(can) not in output:
                  break

      return "".join(candidate)
  ```

# Flag

`Alpaca{l...y}`
