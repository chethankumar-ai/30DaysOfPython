def sum_num(n,res=0):
    for i in n:
        if type(i)==int:
            res+=i
        elif type(i) in [list,tuple,set]:
            res+=sum_num(i)
    return res
print(sum_num(eval(input())))

