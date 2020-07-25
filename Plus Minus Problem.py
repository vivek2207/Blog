from itertools import cycle, chain
from operator import pos, neg


def plus_minus_fast(*, n):
    """Efficient Solution."""
    assert n > 0

    rem = n % 4
    if rem == 1 or rem == 2:
        return None

    pattern = [pos, neg, neg, pos]
    if rem == 0:
        signs = cycle(pattern)
    elif rem == 3:
        signs = chain([neg, neg, pos], cycle(pattern))

    unsigned_nums = range(1, n + 1)
    signed_nums = [
        sign(num) for sign, num in zip(signs, unsigned_nums)
    ]
    return signed_nums
    
for i in range(1, 11):
    print(f"{i:2}  {plus_minus_fast(n=i)}")
