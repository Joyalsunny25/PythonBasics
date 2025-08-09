num=int(input("Enter a number:"))
if num%2==0:
    if 2<=num<=5:
        print("Not Weird")
    elif 6<=num<=20:
        print("Weird")
    elif num>=20:
        print("Not WEird")
else:
    print("Odd")