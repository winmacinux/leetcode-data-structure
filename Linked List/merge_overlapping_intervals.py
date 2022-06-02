class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self) -> str:
        return str(self.first) + " " + str(self.second)


def mergeOverlappingIntervals(A):
    result = []
    result.append(A[0])

    for i in range(1, len(A)):
        # Looped interval
        fi = A[i].first
        si = A[i].second

        # Last selected Interval
        f = result[len(result) - 1].first
        s = result[len(result) - 1].second

        if s >= fi:
            result[len(result) - 1].second = max(si, s)
        else:
            result.append(A[i])

    return result


if __name__ == "__main__":
    V = [
        Pair(1, 5),
        Pair(3, 7),
        Pair(4, 6),
        Pair(6, 8),
    ]

    result = mergeOverlappingIntervals(V)

    for pair in result:
        print(pair)
