# # issquare = lambda x : x**2
# # print(issquare(int(input("Enter the number:"))))


# # write a program to print cude of number is the number is odd or else square
# # x = lambda num : num**2 if num % 2 == 0 else num **3
# # print(x(int(input("Ennter the number: "))))
# # write a program to print the data in reverse order of the data support indexing else print data as it is 
# x = lambda n : n[::-1] if type(n) in [str,list,tuple] else n
# print(x(eval(input("Enter the data: "))))
sum = lambda n1,n2,n3,n4=0,n5=0 : n1+n2+n3+n4+n5
print(sum(1,2,3,4,5))  # output 15


