import math
from typing import List

def divisors(n: int) -> List[int]:
    """Return sorted positive divisors of n. For n == 0 returns an empty list (all integers divide 0)."""
    if n == 0:
        return []
    n = abs(n)
    res = []
    root = int(math.isqrt(n))
    for i in range(1, root + 1):
        if n % i == 0:
            res.append(i)
            j = n // i
            if j != i:
                res.append(j)
    return sorted(res)

if __name__ == "__main__":
    try:
        x = int(input("Enter an integer: ").strip())
    except Exception:
        print("Invalid input")
    else:
        if x == 0:
            print("Every nonzero integer divides 0 (infinite divisors).")
        else:
            print(f"Divisors of {x}: {divisors(x)}")