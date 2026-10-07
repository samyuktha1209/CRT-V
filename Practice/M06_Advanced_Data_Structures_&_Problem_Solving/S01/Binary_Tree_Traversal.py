class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
#Tree Structure
root = Node(1)
root.left = Node(2)
root.right= Node(3)
root.left.left = Node(4)
root.right.right = Node(5)

#Tree Traversal techniques
'''
1. DFS 
     1. pre-order (root - left - right)
     2. in- order (left - root - right)
     3. post - order (left - right- root)
2. BFS(level order)
'''
def Pre_Order(root):
    if root:
        print(root.data,end = "->")
        Pre_Order(root.left)
        Pre_Order(root.right)
print("Pre_Order")
Pre_Order(root)

def In_Order(root):
    if root:
        In_Order(root.left)
        print(root.data,end = "->")
        In_Order(root.right)
print("\n In_Order")
In_Order(root)

def Post_Order(root):
    if root:
        Post_Order(root.left )
        Post_Order(root.right )
        print(root.data,end = "->")
print("\n Post_Order")
Post_Order(root)


from collections import deque
def Level_Order(root):
    if root is None:
        return 
    d = deque([root])
    while d:
        node = d.popleft()
        print(node.data,end="->")
        