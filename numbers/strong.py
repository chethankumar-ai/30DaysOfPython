def strong_num(number):
    num = number
    out = 0
    length = len(str(num))
    for i in str(num):
        out+=pow(int(i),length)
    if out==num:
        return True
    else:
        return False

def strong_between(num1,num2):
    out=[]
    for i in range(num1,num2+1):
        if strong_num(i):
            out+=[i]
    print(out)

strong_between(100,200)