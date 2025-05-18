# l = [123,4+5j,67,'hello','collection']
# out =[6,3,'hll','cllctn']
l = eval(input("Enter the list you want:"))
out =[]
for i in l:
    if type(i) == int:
        sum = 0
        for j in str(i):
            sum+=int(j)
        out.append(sum)
    elif type(i) == str:
        res = ''
        for j in i:
            if j not in 'aeiouAEIOU':
                res+=j
        out+=[res]
print(out)
