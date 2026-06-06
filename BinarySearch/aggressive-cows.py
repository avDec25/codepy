# https://www.spoj.com/problems/AGGRCOW/


# print(f"t = {t}")
# print(f"n = {n}")
# print(f"c = {c}")
# print(f"a = {stalls}")

def can_place(min_dist):
    cows = 1
    last = stalls[0]
    for i in range(1, n):
        if stalls[i] - last >= min_dist:
            cows += 1
            last = stalls[i]
            if cows == c:
                return True
    return False

t = int(input())
while t:
    t -= 1
    n, c = (int(x) for x in input().split(' '))
    stalls = []
    for _ in range(n):
        stalls.append(int(input()))

    stalls.sort()
    lo, hi = 1, stalls[-1] - stalls[0]
    ans = 0
    while lo <= hi:
        mid = (hi + lo) // 2
        if can_place(mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    print(ans)
# 1
# 5 3
# 1
# 2
# 8
# 4
# 9
