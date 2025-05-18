def divisors(num):
    div = []
    for i in range(1,num+1):
        if num%i==0:div.append(i)
    return div
print(divisors(int(input("ENTR THE NUMBER:"))))

