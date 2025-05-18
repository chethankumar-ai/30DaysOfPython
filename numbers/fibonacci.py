def fibonacci(num):
    fs=[0,1]
    for i in range(1,num):
        fs.append(fs[i]+fs[i-1])
    return fs[num]
print(fibonacci(10))
