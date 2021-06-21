num=int(input("enter the number"))
digit=0
while num>0:
    digit=digit+num%10
    num=num//10
print(digit)