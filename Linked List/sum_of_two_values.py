
def sumOfTwo(A, val):
    s = set()
    for a in A:
        if val - a in s:
            return True
        s.add(a)
    return False


if __name__ == "__main__":
    v = [5, 7, 1, 2, 8, 4, 3]
    test = [3, 20, 1, 2, 7]

    for val in test:
        print(sumOfTwo(v, val))
