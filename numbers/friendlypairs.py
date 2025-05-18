def friendly_pairs(num1,num2):
    sum1=0
    sum2=0
    for i in range(1,num1):
        if num1%i==0:
            sum1+=i
    for j in range(1,num2):
        if num2%j==0:
            sum2+=j
    if num1%sum1==num2%sum2:
        return True
    else:
        return False
print(friendly_pairs(6,28))  # True