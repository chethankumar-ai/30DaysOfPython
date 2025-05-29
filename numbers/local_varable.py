a = 10
b = 20
def sam():
    p=45
    q=55
    def inner():
        nonlocal q
        q=88
        print(p,q)
    print(p,q)
    inner()
    print(q)
print(a+b)
sam()