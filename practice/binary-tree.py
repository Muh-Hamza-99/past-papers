# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.right = None
#         self.left = None
#     def insert(self, data):
#         if self.data:
#             if self.data > data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif self.data < data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data
#     def search(self, data):
#         if data < self.data:
#             if self.left is None:
#                 return False
#             else:
#                 return self.left.search(data)
#         elif data > self.data:
#             if self.right is None:
#                 return False
#             else:
#                 return self.right.search(data)
#         else:
#             return True

# def traverse_tree(tree):
#     if tree is None:
#         return
#     else:
#         traverse_tree(tree.right)
#         print(tree.data, end=" ")
#         traverse_tree(tree.left)

# tree = Node("g")
# tree.insert("c")
# tree.insert("b")
# tree.insert("e")
# tree.insert("a")
# tree.insert("d")
# tree.insert("f")
# tree.insert("i")
# tree.insert("h")
# tree.insert("j")
# tree.insert("k")
# traverse_tree(tree)
# print(tree.search("a"))

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    def insert(self, data):
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif self.data < data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def search(self, data) -> bool:
        if self.data > data:
            if self.left is None:
                return False
            else:
                return self.left.search(data)
        elif self.data < data:
            if self.right is None:
                return False
            else:
                return self.right.search(data)
        else:
            return True

def print_tree(tree):
    if tree is None:
        return 
    else:
        print_tree(tree.right)
        print(tree.data, end=" ")
        print_tree(tree.left)

tree = Node("g")
tree.insert("c")
tree.insert("b")
tree.insert("e")
tree.insert("a")
tree.insert("d")
tree.insert("f")
tree.insert("i")
tree.insert("h")
tree.insert("j")
tree.insert("k")
print_tree(tree)
print(tree.search("p"))