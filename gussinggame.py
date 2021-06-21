user=10
while user<=10:
    sum=int(input("guess ho"))
    if user==sum:
        print(sum,"aap jeet gaye")
        user=user+sum
    elif user>=sum:
        print(sum,"apka number chota hai")
    elif user<=sum:
        print(sum,"apka number bada hai")
    else:
        print("check your number")
    sum=sum+1