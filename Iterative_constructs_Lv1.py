Rcount=5
count=0
i=7
lst=[]
while(True):
    if((i%2==1) and (i%3==1) and (i%4==1) and (i%5==1) and (i%6==1)):
        lst.append(i)
        count=count+1
    if count==Rcount:
        break
    i+=7
print(lst[0],lst[1],lst[3])