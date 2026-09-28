import string
import subprocess


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


flag_len = find_flag_len()
flag = find_flag(flag_len=flag_len)  # type: ignore
print("flag -> ", flag)
