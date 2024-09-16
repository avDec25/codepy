def prefixXor(a):
    ans = [a[0]]
    for i in range(1, len(a)):
        ans.append(ans[i-1] ^ a[i])
    return ans


a = [8, 1, 2, 12, 7, 6]
print(prefixXor(a))
