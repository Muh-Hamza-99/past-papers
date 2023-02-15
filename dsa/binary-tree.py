class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item
        self.order_list = []

    def insert(self, item):
        if self.item:
            if item < self.item:
                if self.left is None:
                    self.left = Node(item)
                else:
                    self.left.insert(item)
            elif item > self.item:
                if self.right is None:
                    self.right = Node(item)
                else:
                    self.right.insert(item)
        else:
            self.item = item

    def search(self, item):
        while self.item != item:
            if item < self.item:
                self.item = self.left
            else: 
                self.item = self.right
            if self.item is None:
                return None
        return self.item

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()
        print(self.item, self.right, self.left)

    def traverse(self, tree):
        arr = []
        if tree:
            arr.append(tree.item)
            arr = arr + self.traverse(tree.left)
            arr = arr + self.traverse(tree.right)
        return arr

tree = Node(27)

tree.insert(19)
tree.insert(36)
tree.insert(42)
tree.insert(16)
tree.insert(21)

# print(tree.search(19))

print(tree.traverse(tree))