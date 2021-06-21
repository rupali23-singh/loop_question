num=int(input("enter the number"))
i=num
sum=0
count=len(str(num))
while i>0:
    rem=i%10
    sum=sum+rem**count
    i=i//10
if sum==num:
    print("it is armstrong=")
else:
    print("it is not armstrong=")