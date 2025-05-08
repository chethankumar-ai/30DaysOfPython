# 3.This Method uses bitwise operators to check if a given number is Even or Odd.
def isEven(num):
    return not num & 1
if __name__ =="__main__":
    num = int(input("Enter the number:"))
    if isEven(num):
        print("even")
    else:
        print("Odd")