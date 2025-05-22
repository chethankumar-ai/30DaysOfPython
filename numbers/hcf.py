def get_hcf(num1,num2):
    hcf = 1
    for i in range(1,min(num1,num2)):
        if num1%i==0 and num2%i==0:
            hcf = i
    return hcf
print(get_hcf(12,18))  # output 6

num = int(input("Enter the number: "))
num1= int(input("Enter the number: "))
while num!=num1:
    if num>num1:
        num = num-num1
    else:
        num1 = num1-num
print("HCF is: ",num)
