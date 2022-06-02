# Time Complexity: O(2^n)
# Auxilary Space: O(1)

def knapsack(C, wt, val, n):
    if not n or not C:
        return 0

    # If weight is more than Capacity we cannot pick that item. So need to ignore the weight
    if wt[n - 1] > C:
        return knapsack(C, wt, val, n-1)

    else:
        return max(val[n-1] + knapsack(C - wt[n - 1], wt, val, n - 1), knapsack(C, wt, val, n - 1))


if __name__ == "__main__":
    # Items value and weight
    val = [60, 100, 120]
    wt = [10, 20, 30]

    # Capacity
    C = 50

    n = len(val)

    result = knapsack(C, wt, val, n)
    print(result)
