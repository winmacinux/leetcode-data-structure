import heapq


if __name__ == "__main__":
    A = [3,9,2,1,4,5]
    # heapq._heapify_max(A)
    heapq.heapify(A)
    print(A)
    print(heapq.heappop(A))
    # print(heapq.nsmallest(5, A))
    