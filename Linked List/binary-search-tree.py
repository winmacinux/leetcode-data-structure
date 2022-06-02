
from tkinter import E


class Node:

    def __init__(self, key) -> None:
        self.left = None
        self.key = key
        self.right = None


class BinarySearchTree:
    r = None

    def __init__(self, items=[]) -> None:
        assert len(items), "Empty list of items"
        for (i, key) in enumerate(items):
            if i is 0:
                self.r = self.insert(root=None, key=key)
            else:
                if self.r.key == key:
                    return self.r
                elif self.r.key < key:
                    self.r.right = self.insert(self.r.right, key)
                else:
                    self.r.left = self.insert(self.r.left, key)


    def insert(self, root, key):

        if root is None:
            return Node(key=key)
        else:
            if root.key == key:
                return root
            elif root.key < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)

        return root

    def inorder(self, root):
        if root:
            return self.inorder(root.left) + [root.key] + self.inorder(root.right)
        else:
            return []


    def minValueNode(self, root):
        current = root
        
        while(current.left is not None):
            current = current.left 
        
        return current


    def delete(self, root, key):
        if root is None:
            return root

        if root.key < key:
            root.right = self.delete(root.right, key)
        
        if root.key > key:
            root.left = self.delete(root.left, key)

        else:

            # Single child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # node with both children 
            temp = self.minValueNode(root.right)

            root.key = temp.key

            # Delete the inorder successor from the right subtrees
            root.right = self.delete(root.right, temp.key)

        return root

    def search(self, root, key):
        
        if root is None:
            return root

        if root.key == key:
            return [root.key, root.left and root.left.key, root.right and root.right.key]
        elif root.key < key:
            return self.search(root.right, key)
        else:
            return self.search(root.left, key)


    # Traverse/Sort
    def traverse(self):
        return self.inorder(self.r)

    def add(self, key):
        self.r = self.insert(self.r, key)

    def remove(self, key):
        self.r = self.delete(self.r, key)

    def find(self, key):
        return self.search(self.r, key)
            




if __name__ == "__main__":
    tree = BinarySearchTree(items=[12, 39, 11, 34, 6, 8, 15, 79, 84])
    print(tree.traverse())
    # tree.remove(12)
    print(tree.find(6))
