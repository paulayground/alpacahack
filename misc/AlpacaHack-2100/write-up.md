# Category

misc

# Overview

🦙 < The flag is on the Jan 2100 calendar of Daily AlpacaHack.

# Analysis

문제에서 나와있는 alpacahhack 데일리 캘린더에 2100년 1월에 존재하는 flag를 얻기 위해, 어떤 방식으로 다른 월의 캘린더를 조회하는 지 확인해본 결과, `?month=2026-03`와 같이 `month` 쿼리스트링을 기준으로 이동한다는 것을 알 수 있다.

# Exploitation

1. url을 `https://alpacahack.com/daily?month=2100-01`와 같이 2100년 1월로 변경할 시 해당 년, 월의 캘린더를 볼 수 있는데 11일부터 17일까지 캘린더일정의 내용이 flag형식으로 각 날짜별로 순차적으로 분할 되어 있는 것을 확인할 수 있다.
2. 해당 부분의 html코드를 확인해보면 flag가 적힌 일자들에는 `.css-kdgvf0` 클래스가 적용되어 있으며, 브라우저 콘솔에서 아래 코드를 실행하면 해당 요소들만 불러와 요소안의 내용을 출력하여 완성된 flag를 만들 수 있다.
   ```js
   // document.querySelectorAll(".css-kdgvf0")의 응답은 NodeList이기 때문에 iterator가 없어 Array로 감싸줌
   Array.from(document.querySelectorAll(".css-kdgvf0"))
     // 내용이 포함된 innerText만 리턴
     .map((el) => el.innerText)
     // 모아진 배열을 한 문자열로 합침
     .join("");
   ```

# Flag

`Alpaca{br...e.}`
