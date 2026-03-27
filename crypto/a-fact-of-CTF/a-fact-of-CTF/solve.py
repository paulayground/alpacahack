from collections import Counter

primes = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
    223,
    227,
    229,
    233,
    239,
    241,
    251,
    257,
    263,
    269,
    271,
    277,
    281,
    283,
    293,
]

output = 0
with open("./output.txt") as f:
    output = int(f.read().strip(), 16)


def prime_factorization(n: int):
    """
    소인수 분해
    """
    counts: Counter[int] = Counter()

    for p in primes:
        while n % p == 0:
            counts[p] += 1
            n //= p

        if n == 1:
            break

    return counts


counts = prime_factorization(output)

flag = "".join([chr(counts[i]) for i in counts])

print(flag)
