def decode(s, n):
    if n == 0 or n == 1:
        return 1
    count = 0
    if s[n - 1] > "0":
        count = decode(s, n - 1)
    if s[n - 2] == '1' or (s[n - 2] == '2' and s[n - 2] < '7'):
        count += decode(s, n - 2)
    return count


def decoding(s):
    if len(s) == 0 or (len(s) == 1 and s[0] == '0'):
        return 0
    return decode(s, len(s))


digits = ['1', '2', '1']
print(decoding(digits))
