# adaundant number
def add_number(num):
    sum = 0
    temp = num
    for i in range(1,num):
        if num %i==0:
            sum+=i
    if sum>num:
        print("true")
    else:
        print("false")

add_number(12)