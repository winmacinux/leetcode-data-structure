import collections
LinkedList = collections.deque

class LRU:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = set()
        self.cache_vals = LinkedList()

    def get(self, value):
        if value not in self.cache:
            return None
        else:
            return self.cache_vals.index(value) 

    def insert(self, value):

        add = self.get(value)

        if not add:
            # Check the size of the cache reach to capacity
            if len(self.cache) >= self.capacity:
                self.cache_vals.append(value)
                self.cache.add(value)
                self.cache.remove(self.cache_vals.popleft())
            else:
                self.cache_vals.append(value)
                self.cache.add(value)
        # Move to Recently Used
        else:
            self.cache_vals.remove(value)
            self.cache_vals.append(value)

    def print(self):
        for val in self.cache_vals:
            print(val, ",")

if __name__ == "__main__":
    cache = LRU(4)
    cache.insert(3)
    cache.insert(5)
    cache.insert(1)
    cache.insert(8)
    cache.insert(6)
    cache.insert(5)

    cache.print()


        
