'''
syntax:
type_checking = it is used to check the type of an object.
isinstance(object, type)

what is the output of isinstance()  method?
The `isinstance()` method in Python checks if an object is an instance or subclass of a specified class or type. It returns `True` if the object is an instance of the specified type or a subclass thereof, and `False` otherwise.
'''

'''
a=10
b=15.5
c="Ram"
d=[1,2,3,4,5,6]
e=(1,2,3,10,45,6)
f=(1,2,3,4,5,6)
g={"name":"Kalyani"}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
'''

a=10
b=15.5
c="Ram"
d=[1,2,3,4,5,6]
e=(1,2,3,10,45,6)
f=(1,2,3,4,5,6)
g={"name":"Kalyani"}
print(isinstance(a,int))
print(isinstance(b,float))
print(isinstance(c,str))
print(isinstance(d,list))
print(isinstance(e,tuple))
print(isinstance(f,tuple))
print(isinstance(g,dict))

#checking  with multiple data types
x='Ram'
if isinstance(x,(int,float)):
    print('x is a number')
else:
    print('x is  a string')

#checking of object's class:
class A:
    pass
class B(A):
    pass
b= B()
print(isinstance(b,A))
print(isinstance(b,B))

#Example:
def process(data):
    if isinstance(data,int):
        return data * 2
    elif isinstance(data,str):
        return data.upper()
    elif isinstance(data,list):
        return len(data)
print(process(10))
print(process('Thanu'))
print(process([1, 2, 3, 4, 5]))

