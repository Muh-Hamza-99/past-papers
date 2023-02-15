# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def display(self):
#         current_node = self.head
#         while current_node is not None:
#             print(current_node.data)
#             current_node = current_node.next
#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current_node = self.head
#             while current_node.next is not None:
#                 current_node = current_node.next
#             current_node.next = new_node
#     def insert_at_begin(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#     def insert_in_between(self, target_node, data):
#         if target_node is None:
#             return
#         new_node = Node(data)
#         new_node.next = target_node.next
#         target_node.next = new_node
#     def delete(self, data):
#         current_node = self.head
#         previous_node = self.head
#         while current_node:
#             if current_node.data == data:
#                 if current_node == self.head:
#                     self.head = current_node.next
#                 else:
#                     previous_node.next = current_node.next
#                 return
#             previous_node = current_node
#             current_node = current_node.next

# alphabet = LinkedList()
# alphabet.append("b")
# alphabet.append("c")
# alphabet.append("e")
# alphabet.insert_at_begin("a")
# alphabet.insert_in_between(alphabet.head.next.next, "d")
# alphabet.delete("b")
# alphabet.display()

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def print(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end="   ")
            current_node = current_node.next
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(data)
    def delete(self, data):
        current_node = self.head
        previous_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node == self.head:
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next
                return
            previous_node = current_node
            current_node = current_node.next

alphabet = LinkedList()
alphabet.append("b")
alphabet.append("c")
alphabet.append("e")
alphabet.print()