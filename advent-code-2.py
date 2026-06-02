def is_repeated_substring_at_least_twice(s):
    """
    Returns True if the entire string is composed of a repeated substring
    that repeats at least 2 times.
    For example: "abcabc" is composed of "abc" repeated 2 times → True
                 "abcabcabc" is composed of "abc" repeated 3 times → True
                 "abc" is not repeated (appears 1 time) → False
    
    Args:
        s (str): The input string to check
        
    Returns:
        bool: True if the entire string is made of repeated substrings 
              at least 2 times, False otherwise
    """
    n = len(s)
    
    if n < 2:
        return False
    
    # Check all possible substring lengths that can divide the string evenly
    # Maximum length is n//2 because we need at least 2 repetitions
    for length in range(1, n // 2 + 1):
        # The substring length must divide the total length evenly
        if n % length == 0:
            repetitions = n // length
            # Check if repetitions is at least 2
            if repetitions >= 2:
                pattern = s[:length]
                # Check if repeating this pattern gives us the original string
                if pattern * repetitions == s:
                    return True
    
    return False


# Alternative efficient approach using string manipulation
def is_repeated_substring_at_least_twice_v2(s):
    """
    Alternative approach: Check if the string appears in (s+s)[1:-1]
    This works because if a string is made of repeating patterns (at least twice),
    it will appear in the doubled string with first and last char removed.
    
    Args:
        s (str): The input string to check
        
    Returns:
        bool: True if the entire string is made of repeated substrings 
              at least 2 times, False otherwise
    """
    if len(s) < 2:
        return False
    
    return s in (s + s)[1:-1]


# Function to find the smallest repeating pattern (at least 2 repetitions)
def find_repeating_pattern_at_least_twice(s):
    """
    Returns the smallest substring that repeats at least twice to form the entire string.
    Returns None if no such pattern exists.
    
    Args:
        s (str): The input string to check
        
    Returns:
        tuple or None: (pattern, repetitions) or None if no pattern exists
    """
    n = len(s)
    
    if n < 2:
        return None
    
    for length in range(1, n // 2 + 1):
        if n % length == 0:
            repetitions = n // length
            if repetitions >= 2:
                pattern = s[:length]
                if pattern * repetitions == s:
                    return (pattern, repetitions)
    
    return None


# Function to find all possible patterns (at least 2 repetitions)
def find_all_repeating_patterns_at_least_twice(s):
    """
    Returns all substrings that repeat at least twice to form the entire string.
    
    Args:
        s (str): The input string to check
        
    Returns:
        list: List of tuples (pattern, repetitions)
    """
    n = len(s)
    patterns = []
    
    if n < 2:
        return patterns
    
    for length in range(1, n // 2 + 1):
        if n % length == 0:
            repetitions = n // length
            if repetitions >= 2:
                pattern = s[:length]
                if pattern * repetitions == s:
                    patterns.append((pattern, repetitions))
    
    return patterns


with open("submission-test.txt", "r") as file:    
    solution = 0
    for id_range in file.readline().split(","):
        lo, hi = id_range.split("-")
        lo = int(lo)
        hi = int(hi)
        invalid_id = []
        while lo <= hi:
            if is_repeated_substring_at_least_twice(str(lo)):
                invalid_id.append(lo)
                solution += lo
            lo += 1
        print(invalid_id)
    print(solution)