from functools import lru_cache


@lru_cache(maxsize=None)
def count_ways(n):
    if n == 1 or n == 0:
        return 1
    if n < 0:
        return 0

    return count_ways(n - 1) + count_ways(n - 2)


n = 4
print(count_ways(n))
