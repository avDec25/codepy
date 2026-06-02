def find_max_n_digit_number(num_str, n=12):
    if isinstance(num_str, int):
        num_str = str(num_str)
    
    if len(num_str) < n:
        return None
    
    result = []
    start = 0
    
    for i in range(n):
        remaining_needed = n - i - 1        
        end = len(num_str) - remaining_needed        
        max_digit = max(num_str[start:end])        
        max_index = num_str.index(max_digit, start, end)        
        result.append(max_digit)        
        start = max_index + 1
    
    return ''.join(result)


def find_max_twelve_digit_number(num_str):
    return find_max_n_digit_number(num_str, 12)


ans = 0
with open("test.txt", "r") as file:
    for line in file.readlines():
        mx_num = find_max_twelve_digit_number(line)
        print(line)
        print(mx_num)
        print("-------------------")
        ans += int(mx_num)
print(ans)