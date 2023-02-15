class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

# print(node1.data)
# print(node1.next.data)
# print(node1.next.next.data)

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_in_between(self, target_node, data):
        if target_node is None:
            return
        new_node = Node(data)
        new_node.next = target_node.next
        target_node.next = new_node
    def delete(self, data):
        current_node = self.head
        previous_node = self.head
        while current_node:
            if current_node.data == data:
                if current_node == self.head:
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next
                return
            previous_node = current_node
            current_node = current_node.next


days_of_week = LinkedList()
days_of_week.append("Tue")
days_of_week.append("Wed")
days_of_week.append("Fri")
days_of_week.insert_at_begin("Mon")
days_of_week.insert_in_between(days_of_week.head.next.next, "Thurs")
days_of_week.delete("Wed")
# monday = Node("Mon")
# tuesday = Node("Tue")
# wednesday = Node("Wed")
# days_of_week.head = monday
# days_of_week.head.next = tuesday
# tuesday.next = wednesday

# print(days_of_week.head.data)
# print(days_of_week.head.next.data)
# print(days_of_week.head.next.next.data)

# current=self.head 

#     prev=self.head 

#     while current: 

#       if current.data==data: 

#         if current==self.head: 

#           self.head=current.next 

#         else: 

#           prev.next=current.next 

#         return 

#       prev=current 

#       current=current.next

current_node = days_of_week.head
while current_node is not None:
    print(current_node.data)
    current_node = current_node.next