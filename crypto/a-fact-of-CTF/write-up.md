# Category

crypto

# Overview

The very first challenge ever completed for AlpacaHack was never released because we adjusted the difficulty for the first Crypto round. (Organizers' note)

# Analysis

- 300보다 작은 소수들이 주어지며 flag의 길이를 반복하면서 주어진 소수와 제곱하여 최종 결과에 연속적으로 곱해진다.

- output.txt에 임의의 flag값을 소수와 제곱하여 곱해진 값을 소인수분해하게되면 소수의 기준으로 flag의 ASCII 코드값만큼 곱한 것을 알 수 있는데, 예를 들어 ASCII 코드 `97`인 단어 `a`를 소수 첫번째 값인 `2`와 연산되었다 가정하면 소인수 분해 시 $2^{97}$인 값이 곱해져있는 것을 알 수 있다.

# Exploitation

결과값인 output을 소인수분해 후 생겨난 지수들의 값을 ASCII 코드에 맞춰 변환하면 flag를 획득할 수 있다.

```py 
# solve.py
def prime_factorization(n: int):
    """
    소인수 분해
    """
    factors: List[int] = []

    for p in primes:
        while n % p == 0:
            factors.append(p)
            n //= p

        if n == 1:
            break

    return factors

factorized_primes = prime_factorization(output)

# 개수를 세주기 위함
counts: Counter[int] = Counter(factorized_primes)

# ASCII 문자열로 변경
flag = "".join([chr(counts[i]) for i in counts])
```

# Flag

`Alpaca{pr...ng}`
