def cutRod(p, index, n):
    if index == 0:
        return n * p[0]
    if n == 0:
        return 0
    nocut = cutRod(p, index - 1, n)
    cut = float('-inf')
    rod_len = index + 1
    if rod_len <= n:
        cut = p[index] + cutRod(p, index, n - rod_len)

    return max(cut, nocut)


arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Value is ", cutRod(arr, size - 1, size))
