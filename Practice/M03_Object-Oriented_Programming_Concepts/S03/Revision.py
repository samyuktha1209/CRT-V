
'''
take a family tree and apply all 5 types of inheritance
'''
#1. Single Inheritance
class Grandparent:
    def __init__(self, name):
        self.name = name

    def display_grandparent(self):
        print(f"Grandparent: {self.name}")
#2. Multi-level Inheritance
class Parent(Grandparent):
    def __init__(self, name, parent_name):
        super().__init__(name)
        self.parent_name = parent_name

    def display_parent(self):
        print(f"Parent: {self.parent_name}")
        self.display_grandparent()
#3. Multiple Inheritance
class Uncle:
    def __init__(self, uncle_name):
        self.uncle_name = uncle_name

    def display_uncle(self):
        print(f"Uncle: {self.uncle_name}")
    def display_family(self):
        print(f"Family: {self.uncle_name}")
        self.display_uncle()
#4. Hierarchical Inheritance
class Sibling(Parent):
    def __init__(self, name, parent_name, sibling_name):
        super().__init__(name, parent_name)
        self.sibling_name = sibling_name

    def display_sibling(self):
        print(f"Sibling: {self.sibling_name}")
        self.display_parent()
#5. Hybrid Inheritance
class Cousin(Uncle, Sibling):
    def __init__(self, name, parent_name, sibling_name, cousin_name):
        Uncle.__init__(self, cousin_name)
        Sibling.__init__(self, name, parent_name, sibling_name)

    def display_cousin(self):
        print(f"Cousin: {self.uncle_name}")
        self.display_family()
        self.display_sibling()


class A:
    def S(self):
        print('A')
class B(A):
    def S(self):
        print('B')
def K(Shape):
    Shape.S()
a=A()
b=B()
k(a)
k(b)

a = 10
