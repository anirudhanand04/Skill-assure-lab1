numberInWords = ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
print(numberInWords[0:])
print(numberInWords[:3])
print(numberInWords[1:3])
print(numberInWords[1:-1])
print(numberInWords[-4:-2])
print(numberInWords[5])
print("\n")
#2
emp1 = [1001,'James' ,25,'developer']
emp2 = [1002, 'Richa', 30,'Tester']
emp3 = [1003, 'Herald', 26,'BA']
print([emp1,emp2,emp3])
print("\n")
#3
num = [45,56,78,89,90]
num.insert(2,78)
print(num)
num.remove(45)
print(num)
num.pop(1)
print(num)
num.pop()
print(num)
del(num[3:])
print(num)
num.extend([5,6,7])
print(num)
min(num)
print(num)
max(num)
print(num)
sum(num)
print(num)
num=num.sort()
print(num)
