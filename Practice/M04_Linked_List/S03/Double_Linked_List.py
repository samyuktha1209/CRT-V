class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
#2.Insert the data into the nodes
Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(30)
Node4 = Node(40)
#3.Generate the Connection btw the nodes
Node1.next = Node2
Node2.prev = Node1
Node2.next = Node3
Node3.prev = Node2
Node3.next = Node4
Node4.prev = Node3
#4.Traverse all the nodes
def traverse():
    curr=Node1
    while curr:
        print(curr.data,end=" <-> ")
        curr=curr.next
    print("None")
traverse()
#write a function to traverse the nodes in reverse order
def traverse_reverse():
    curr=Node4
    while curr:
        print(curr.data,end=" <-> ")
        curr=curr.prev
    print("None")
traverse_reverse()

'''


class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
def insert_begin(head,data):
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node
def insert_after(node,data):
    if node is None:
        print("Error")
        return
    new_node=Node(data)
    new_node.prev=node
    new_node.next=node.next
    if node.next:
        node.next.prev=new_node
    node.next=new_node

def insert_end(head,data):
    new_node = Node(data)
    if head ==None:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    new_node.prev = curr
    return head
def traverse(head):
    curr = head
    while curr:
        print(curr.data,end = "<->")
        curr = curr.next
    print("None")
head = None
head = insert_begin(head,10)
head = insert_begin(head,20)
head = insert_begin(head,50)
print("Insertion at the begin")
traverse(head)
print()
'''
#Insertion at pos
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def insert_after(node, data):
    if node is None:
        print("Error")
        return None

    new_node = Node(data)

    new_node.prev = node
    new_node.next = node.next

    if node.next:
        node.next.prev = new_node

    node.next = new_node

    return new_node


def insert_before(node, data):
    if node is None:
        print("Error")
        return None

    new_node = Node(data)

    new_node.next = node
    new_node.prev = node.prev

    if node.prev:
        node.prev.next = new_node

    node.prev = new_node

    return new_node


def traverse(head):
    curr = head

    while curr:
        print(curr.data, end="<->")
        curr = curr.next

    print("None")


# Creating nodes
head = Node(10)

# Insertion after
insert_after(head, 20)
insert_after(head.next, 50)

print("Insertion After:")
traverse(head)

print()

# Insertion before
new_head = insert_before(head, 5)
head = new_head

new_head = insert_before(head, 2)
head = new_head

print("Insertion Before:")
traverse(head)

#Deletion at the begining





















































