# Decimal to binary 
def dec_bin(num):
    binary=[]
    while num>0:
        binary.append(num%2)
        num=num//2
    for i in reversed(binary):
        print(i,end='')
dec_bin(2)