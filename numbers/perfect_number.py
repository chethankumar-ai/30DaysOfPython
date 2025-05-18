def perfect_num(num):
    temp = num
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == temp:
        return True
    else:
        return False
print(perfect_num(int(input("Enter the number:"))))
