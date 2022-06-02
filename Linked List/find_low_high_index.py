def findLowIndex(A, key):

    low = 0
    high = len(A) - 1
    mid = high // 2

    while low <= high:

        midValue = A[mid]

        if midValue < key:
            low = mid + 1
        else:
            high = mid - 1

        mid = low + (high - low) // 2

    if low < len(A) and A[low] == key:
        return low

    return -1


def findHighIndex(A, key):

    low = 0
    high = len(A) - 1
    mid = high // 2

    while low <= high:

        midValue = A[mid]

        if midValue <= key:
            low = mid + 1
        else:
            high = mid - 1

        mid = low + (high - low) // 2

    if high == -1:
        return high

    if high < len(A) and A[high] == key:
        return high
    
    return -1



if __name__ == "__main__":
    array = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3,
             4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
    key = 5
    print(findLowIndex(array, key))
    print(findHighIndex(array, key))
