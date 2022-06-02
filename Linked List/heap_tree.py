# The running time complexity of the building heap is O(n log(n)) 
# where each call for heapify costs O(log(n)) 
# and the cost of building heap is O(n). 
# Therefore, the overall time complexity will be O(n log(n)).

# Applications of Heap
#     - while implementing priority queue
#     - Heap sort
#     - Dijkstra's algorithm
#     - in operating system for the job scheduling algorithm
#     - selection algorithm
#     - prim’s algorithm
#     - order statistics
#     - k-way merge


class Node:

    def __init__(self, key):
        self.right = None
        self.value = key
        self.left = None


class HeapTree:

    def left(self, k):
        return 2*k + 1

    def right(self, k):
        return 2*k + 2

    def max_heapify(self, A, k):
        l = self.left(k)
        r = self.right(k)

        largest = k

        if l < len(A) and A[l] > A[k]:
            largest = l

        if r < len(A) and A[r] > A[k]:
            largest = r

        if largest != k:
            A[k], A[largest] = A[largest], A[k]
            self.max_heapify(A, largest)

    def min_heapify(self, A, k):
        l = self.left(k)
        r = self.right(k)

        smallest = k

        if l < len(A) and A[l] > A[k]:
            smallest = l

        if r < len(A) and A[r] > A[k]:
            smallest = r

        if smallest != k:
            A[k], A[smallest] = A[smallest], A[k]
            self.min_heapify(A, smallest)

    def build_max_heap(self, A):
        n = int((len(A)//2)-1)
        for k in range(n, -1, -1):
            self.max_heapify(A, k)
    
    def build_min_heap(self, A):
        n = int((len(A)//2)-1)
        for k in range(n, -1, -1):
            self.min_heapify(A, k)


if __name__ == "__main__":
    tree = HeapTree()
    A = [3,9,2,1,4,5]
    B = [3,9,2,1,4,5]
    tree.build_max_heap(A)
    tree.build_min_heap(B)

    print(A)
    print(B)