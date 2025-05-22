# Convert into hexadecimal
def hexa_decimal(hexa_decimal):
    decimal = 0
    power = 0
    for i in hexa_decimal:
        if '0'<=i<='9':
            decimal+=int(i) *pow(16,power)
            power+=1
        elif 'A' <= i<= 'F':
            n = ord(i) - 55
            decimal+=n*pow(16,power)
            power+=1
    print(decimal)
X=input("Enter the hexa decimal ")
hexa_decimal(X)


