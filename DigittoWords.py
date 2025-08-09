number={
    
    1:"One",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"Six",
    7:"Seven",
    8:"eight",
    9:"Nine",
    10:"Ten"

}
num=int(input("Enter the number between 1-10"))
# print(number[num]) key value pair vechollath,using in key word thazhe
if num in number:
    print (number[num])
else:
    print("Eror")  