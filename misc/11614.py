n = int(input())
for _ in range(n):
    w = int(input())
    i = 1
    while w >= 0:
        w -= i
        i += 1

    print(i)

# 6 3 6 7 8 9 10
#    2, 3, 3, 3, 3, 4