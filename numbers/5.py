# Method 3 : Using Recursion sum of N numbers
def getSum(num):
    if num==1:
        return 1
    return num + getSum(num-1)
print(getSum(int(input("Enter the number:"))))
