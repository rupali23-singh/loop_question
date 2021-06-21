num=int(input("enter the number"))
i=0
a=1
sum=0
count=1
while count<num:
    count=count+1
    i=a
    a=sum
    sum=i+a
print(sum)