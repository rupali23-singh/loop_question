num=int(input("enter the number"))
a=num
i=0
while a>0:
    z=a%10
    i=i+z
    a=a//10
if num%i==0:
    print("it is harshad number=")
else:
    print("it is not harshad number=")