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

mark=int(input("Enter the mark:"))
if mark>=95:
    print("Excellent")
    print("You secured A+")
elif mark>=75:   #elif can be used many times like this to give condition
    print("Good")
    print("You secured B")
else:     #we cannot give a condition is else,it means if it is not ture print this
    print("Sorry Failed")
    print("Work Hard")