from typing import List


def majority_element(a: List[int]) -> int:
    majority = a[0]
    count = 0
    for i in range(1, len(a)):
        if a[i] == majority:
            count += 1
        else:
            count -= 1

        if count < 0:
            majority = a[i]
            count = 0

    return majority


nums = [3, 2, 3]
print(majority_element(nums) == 3)

nums = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums) == 2)