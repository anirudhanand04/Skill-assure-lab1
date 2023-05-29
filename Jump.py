#1
def print5():
    i=1
    print(i)
    while(True):
        i+=1
        if i>5:
            break
        else:
            print(i)
print5()
print("\n")

#2
number=0
for number in range(10):
    if number ==5:
        break
    print('Number is ' + str(number))
print('Out of loop')
print("\n")

#3
for number in range(10):
    if number==5:
        pass
    print('Number is ' + str(number))
print('Out of loop')
print("\n")

#4
for number in range(10):
    if number==5:
        continue
    print('Number is ' + str(number))
print('Out of loop')
print("\n")