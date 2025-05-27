def dec_hexa(num):
    hexa = []
    while num !=0:
        x=num%16
        if x<10:
            hexa.append(chr(x+48))
        else:
            hexa.append(chr(x+55))
        num//=16
    hexa.reverse()
    return''.join(hexa)


print(dec_hexa(12345))