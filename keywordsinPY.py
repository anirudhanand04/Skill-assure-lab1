# KEYWORDS IN PYTHON

# True False
print(5==5)
print(5>5)
print("\n")

# None
print(None == 0)
print(None == False)
print(None == [])
print(None == None)
print("\n")

# void
def a_void_function():
    a = 1
    b = 2
    c = a+b
x = a_void_function()
print("\n")

# and, or, not
print(True and False)
print(True or False)
print(not False)
print("\n")
# as
import math as myMath
print(myMath.cos(myMath.pi))
print("\n")
# assert
#assert 5>5
#assert 5==5
print("\n")
# break
for i in range(1,11):
    if i==5:
        break
    print(i)
print("\n")
# continue
for i in range(1,8):
    if i==5:
        continue
    print(i)
print("\n")
# class
class ExampleClass:
    def function1(parameters):
        print("function1() executing...")
    def function2(parameters):
        print("function2() executing...")
ob1 = ExampleClass()
ob1.function1()
ob1.function2()
print("\n")
# def
def function_name(parameters):
    pass
function_name()
print("\n")
# del
a = 10
print(a)
del a
print(a)
print("\n")
# if..elif..else
num = 2
if num==1:
    print('One')
elif num==2:
    print('Two')
else:
    print('Something else')
print("\n")
# try..raise..catch..finally
try:
    x = 9
    raise ZeroDivisionError
except ZeroDivisionError:
    print('Executed Successfully')
print("\n")
# for
for i in range(1,10):
    print(i)
print("\n")
# from..import
import math
from math import cos
print(math.cos(5))
print("\n")
#global
globalvar = 10
def read1():
    print(globvar)
def write1():
    global globvar
    globvar = 5
def write2():
    globvar = 15
read1()
write1()
read1()
write2()
read1()
print("\n")
# in
a = [1,2,3,4]
print(4 in a)
print("\n")
# is
print (True is True)
print("\n")
# Lambda
a = lambda x:x*2
for i in range(1,6):
    print(a(i))
print("\n")
# nonlocal
def outer_function():
    a = 5
    def inner_function():
        nonlocal a
        a = 10
        print("Inner function: ",a)
    inner_function()
    print("Outer function:",a)
outer_function()
print("\n")
# pass
def function(args):
    pass
print("\n")
# return
def func_return():
    a = 10
    return a
print(func_return())
print("\n")
# while
i = 5
while(i>0):
    print(i)
    i-=1
print("\n")
# with
with open('example.txt','w') as my_file:
    my_file.write('Hello world!')
print("\n")
# yield
def generator():
    for i in range(6):
        yield i*i
g = generator()
for i in g:
    print(i)

print("\n")