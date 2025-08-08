"""
Syntax

if condition:
     statements
"""
# age=int(input("Enter the age"))
# if age>=18:
#     print("Eligible for Voting")
# else:
#     print("not elibile")

# mark=int(input("Enter the mark:"))
# if mark>=95:
#     print("Excellent")
#     print("You secured A+")
# elif mark>=75:   #elif can be used many times like this to give condition
#     print("Good")
#     print("You secured B")
# else:     #we cannot give a condition is else,it means if it is not ture print this
#     print("Sorry Failed")
#     print("Work Hard")

"""
age=int(input("Enter your age:"))
if age>=60:
    c=input("Do you have a membership card(Yes/No):")
    is_member=True if c=="Yes" else False
    if is_member:
        print("You will get 50% Discount")
    else:
        print("You have 20% Discount")
else:
    print("You are not eligible for Discount")
    
    """
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("Enter your choice:")
print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division")
choice=int(input("Enter Your Choice:"))
if choice==1:
    print("Result is:",a+b)
elif choice==2:
    print("Result is:",a-b)
elif choice==3:
    print("Result is:",a*b)
elif choice==4:
    print("Result is:",a/b)
else:
    print("Invalid Input")