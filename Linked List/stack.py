# ADT of stack
from inspect import stack


class ListStack:
    stack = []
    _size = 0
    _top = -1

    def __init__(self, size):
        self._size = size

    def __str__(self):
        assert not self.isEmpty(), "Stack is empty"
        return ', '.join(list(map(str, self.stack[:self._top+1])))
        # return ', '.join([str(self.stack[value]) for value in range(0, self._top + 1)])

    def size(self):
        return self._top + 1

    def isFull(self):
        return True if self._top == self._size - 1 else False

    def isEmpty(self):
        return True if self._top == -1 else False

    def pop(self):
        assert not self.isEmpty(), "Stack is empty"
        self._top = self._top - 1
        return self.stack[self._top]

    def push(self, item):
        assert not self.isFull(), "Stack is full"
        self._top = self._top + 1
        self.stack.insert(self._top, item)

    def traverse(self):
        print(self.stack.__str__())

if __name__ == "__main__":
    try:
        s1 = ListStack(size=4)
        s1.push(4)
        s1.push(5)
        s1.push(3)
        s1.traverse()
    except AssertionError as e:
        print("AssertionError:", e.__str__())
