import subprocess

img = bytes.fromhex(input("hex bytes> "))

mime = subprocess.check_output(
    ["file", "--mime-type", "-b", "-"],
    input=img
).decode().strip()

if not mime.startswith("image/"):
    print("This doesn't look like an image...")
    exit()

exec(img)