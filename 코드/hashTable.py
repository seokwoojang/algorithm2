class Node:
    def __init__(self, item: int, link = None):
        self.item = item
        self.link = link

class HashTable:
    def __init__(self):
        self.size = 3
        self.table = [None] * self.size
    
    def print_table(self) -> None:
        for i, root in enumerate(self.table):
            items = []
            while root:
                items.append(root.item)
                root = root.link
            print(i, end = ' : ')
            print('->'.join(map(str, items)))
    
    def add(self, item: int) -> None:
        if self.table[item % self.size] is None:
            self.table[item % self.size] = Node(item)
            return
        prev = self.table[item % self.size]
        while prev.link:
            prev = prev.link
        prev.link = Node(item)
    
    def remove(self, item: int) -> None:
        if self.table[item % self.size] is None:
            return
        prev = self.table[item % self.size]
        while prev.link:
            if prev.link.item == item:
                prev.link = prev.link.link
                break

ht = HashTable()
for i in range(10 + 1):
    ht.add(i)
ht.print_table()