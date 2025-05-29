x= lambda x: x**2
print(x(3))
sqr =lambda x: x**2
print(sqr(4))
x = lambda x: x**2 if x/2== 0 else x**3
print(x(2))  # output 4
print(x(3))  # output 27
x= lambda n: n[::-1] if type(n) in[str, list, tuple] else n
print(x("hello"))  # output "olleh"
print(x([1, 2, 3]))  # output [3, 2, 1]
print(x(1))  # output (3, 2, 1)
x= lambda n1,n2,n3,n4=0,n5=0:n1+n2+n3+n4+n5
print(x(1, 2, 3))  # output 6
print(x(1, 2, 3, 4))  # output 10
print(x(1, 2, 3, 4, 5))  # output 15
