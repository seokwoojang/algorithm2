
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root == None:
                self.root = Node(key)

        self.current = self.root
        
        while True:
            if self.current.val < key:
                if self.current.right == None:
                    self.current.right = Node(key)
                    break
                else:
                    self.current = self.current.right
            else:
                if self.current.left == None:
                    self.current.left = Node(key)
                    break
                else:
                    self.current = self.current.left

    def search(self, key):
        self.current = self.root

        while True:
            if self.current == None:
                return False

            if self.current.val == key:
                return True
            else:
                if self.current.val < key:
                    self.current = self.current.right
                else:
                    self.current = self.current.left


bst = BST()
bst.insert(7)
bst.insert(3)
bst.insert(4)
print(bst.search(4))