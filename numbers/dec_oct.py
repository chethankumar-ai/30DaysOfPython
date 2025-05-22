# decimal to oct
def dec_oct(num):
    octal=[]
    while num>0:
        octal.append(num%8)
        num//=8
    for i in reversed(octal):
        print(i,end='')
    
dec_oct(234)
