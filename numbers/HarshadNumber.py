# Harshad Number 21 the individual digits of 21 are 2 and 1
# 2+1=3
# 21 is divisible by 3
def is_harshad(num):
    sum = 0
    temp = num
    while temp >0:
        sum += temp % 10
        temp //= 10
    if num % sum == 0:
        return True
    else:
        return False        
    