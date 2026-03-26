# Category

reversing

# Overview

Even if an expression looks complex, it may be an optimized form of a simpler expression.

# Analysis

제시된 `chal.c`의 코드는 사용자가 34자리의 값을 입력할 경우, 입력한 값을 정의된 계산로직을 실행해 나온 결과와 코드네 `table`변수에 정의된 내용과 비교하여 일치할 경우 flag를 응답하는 코드이다.

# Exploitation

1. 테이블이 `char`타입으로 정의가 되어 있기 때문에 1바이트의 값인 256까지 반복하여 코드와 동일한 계산로직을 통해 나온 결과를 확인하여 일치할 경우만 따로 모아 확인하는 방식으로 flag를 획득할 수 있다.

   ```c solve.c
   ...

   char corrects[35];

     for (int i = 0; i < TABLE_SIZE; i++) {
       // char 타입이기 때문에 1바이트의 숫자값 256까지 반복
       for (int j = 0; j < 256; j++) {
         // 문제에서 검증하는 식과 동일한 방식으로 정답 유추
         uint64_t x = (uint8_t)j;
         uint64_t y = (x * 3435973837) >> 34;
         uint64_t t = (x * 613566757) >> 32;
         uint64_t z = x - ((((x - t) >> 1) + t) >> 2) * 7;

         // 테이블에 일치하는 y, z를 찾은 경우 corrects에 넣기
         if (y == table[i][0] && z == table[i][1]) {
           corrects[i] = x;
           break;
         }
       }
     }
     printf("%s\n", corrects);

   ...
   ```

2. 추출된 값을 컴파일된 chal에 실행하여 입력했을 때 `Correct!`와 함께 플래그가 올바르다는 것을 확인할 수 있다.

# Flag

`Alpaca{Di...on}`
