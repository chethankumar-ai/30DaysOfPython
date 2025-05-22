# 2. Python Program to Check Whether a Number is Even or Odd
# num = int(input( "Enter the number:"))
# if num == 0:
#     print("not even or odd")
# elif num %2 == 0:
#     print("Even")
# else:
#     print("Odd")
# using lambda function even or not
iseven = lambda x : x % 2 == 0
print(iseven(int(input("Enter the number:"))))