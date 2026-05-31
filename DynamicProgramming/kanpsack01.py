def knapsack(W: int, w: list[int], v: list[int]) -> int:
    n = len(w)
    T = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            # current item is i-1 and its weight = w[i-1]
            # because we need dummy 0s at top and left
            # since, j is the bag capacity,
            # the current item cannot be taken because its weight is more
            if w[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = max(v[i - 1] + T[i - 1][j - w[i - 1]], T[i - 1][j])
            # all operation in this if else
            # is for knapsack with bag capacity = j
            # so j is never subtracted by 1
            # its is only that previous best is picked up to carry forward
            # which is j - w[i-1]
    return T[n][W]


# https://algo.monster/problems/knapsack_intro
weights = [3, 4, 7]
values = [4, 5, 8]
max_weight = 7
print(knapsack(max_weight, weights, values))  # 9

weights = [10, 20, 30]
values = [60, 100, 120]
max_weight = 50
print(knapsack(max_weight, weights, values))  # 220
