i=2
sum=1
n=int(input("enter the number"))
while i<=n//2:
    if n%i==0:
        sum+=i
    i+=1
if sum==n:
    print(n,"is perfect number=")
else:
    print(n,"is not a perfect number=")