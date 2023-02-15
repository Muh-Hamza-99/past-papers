import collections

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
    def search(self, data):
        if data < self.data:
            if self.left is None:
                return f"{data} search returned no value!"
            return f"{self.left.search(data)} left!"
        elif data > self.data:
            if self.right is None:
                return f"{data} search returned no value!"
            return f"{self.right.search(data)} right!"
        else:
            print(f"{self.data} is found!")

def in_order_print(tree):
    if tree is None:
        return
    else:
        in_order_print(tree.right)
        print(tree.data, end=" ")
        in_order_print(tree.left)

def pre_order_print(tree):
    if tree is None:
        return
    else:
        print(tree.data, end=" ")
        pre_order_print(tree.left)
        pre_order_print(tree.right)

def post_order_print(tree):
    if tree is None:
        return
    else:
        print(tree.data, end=" ")
        post_order_print(tree.right)
        post_order_print(tree.left)

def make_list(tree):
    if tree is None:
        return
    else:
        dictionary[tree.data] = []
        make_list(tree.left)
        if tree.left:
            dictionary[tree.data].append(tree.left.data)
        if tree.right:
            dictionary[tree.data].append(tree.right.data)
        make_list(tree.right)
    return dictionary

def breath_first_search(adjacency_list):
    queue = collections.deque("g")
    visited = []
    while queue:
        node = queue.popleft()
        visited.append(node)
        [queue.append(x) for x in adjacency_list[node]]
        # for x in adjacency_list[node]:
        #     queue.append(x)
    print(visited)

def depth_first_search(adjacency_list):
    stack = ["g"]
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            [stack.append(x) for x in adjacency_list[node]]
    print(visited)

if __name__ == "__main__":
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

    # dictionary = {}
    # adjacency_list = make_list(tree)
    # for i in adjacency_list:
    #     print(f"{i} : {adjacency_list[i]}")
    # breath_first_search(adjacency_list)
    # depth_first_search(adjacency_list)
    # print(tree.search("g"))

in_order_print(tree)
print("\n")
pre_order_print(tree)
print("\n")
post_order_print(tree)