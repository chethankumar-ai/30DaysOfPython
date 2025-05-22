def binary_to_decimal(binary):
    decimal = 0
    base = 1
    while binary > 0:
        rem = binary%10
        decimal +=rem*base
        binary = binary//10
        base = base*2
    return decimal
print(binary_to_decimal(110))



# another method
binary=input()
b=binary[::-1]
decimal=0
for i in range(len(binary)):
    decimal=decimal+int(b[i])*(2**i)
print(decimal)