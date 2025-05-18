# strong number
def strong_num(num):
    sum = 0
    temp = num
    while temp>0:
        digit =temp%10
        fact = 1
        for i in range(1,digit+1):
            fact = fact*i
        sum +=fact
        temp = temp//10
    if sum == num:
        return True
    else:
        return False
# Test the function
num = int(input("Enter a number: "))
if strong_num(num):
    print(f"{num} is a Strong number.")
else:
    print(f"{num} is not a Strong number.")