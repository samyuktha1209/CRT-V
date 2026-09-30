class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Double_LL:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)

        new_node.next = self.head

        if self.head:
            self.head.prev = new_node

        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = new_node
        new_node.prev = curr

    def traverse(self):
        curr = self.head

        while curr:
            print(curr.data, end="<->")
            curr = curr.next

        print("None")

    def delete_begin(self):
        if self.head is None:
            print("Error: List is empty")
            return None
        new_head = self.head
        self.head = self.head.next
        del new_head
    def deletion_end(self):
        if self.head is None:
            print("Error: List is empty")
            return None
        #LL with single node
        if self.head.next is None:
            self.head = None
            return 
        temp = self.head
        while temp.next.next:
            temp = temp.next
        del_node = temp.next
        temp.next.prev = None
        temp.next = None
        del del_node

    def countNodes(self):
        if self.head is None:
            return 0
        if self.head.next is None:
            return 1
        count = 0
        temp = self.head
        while temp:
            count+=1
            temp = temp.next
        return count
    def deletion_Pos(self,data):
        

        

dll = Double_LL()
dll.insert_begin(10)
dll.insert_begin(20)
dll.insert_begin(30)
dll.traverse()
dll.insert_end(40)
dll.insert_end(50)
dll.traverse()
dll.delete_begin()
dll.traverse()
print(dll.countNodes())


