def octal_to_decimal(oct):
    dec = 0
    base = 1
    while oct:
        rem = oct%10
        dec+=rem*base
        base*=8
        oct//=10
    return dec
print(octal_to_decimal(128))



