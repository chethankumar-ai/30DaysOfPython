# # s = "hai hello"
# # print(s.endswith('o'))
# var = input("Enter the number:")
# sum = 0
# for i in var:
#     sum+=int(i)
# print(sum)
# num = 253
# sum = 0
# while num!=0:
#     sum+=num%10
#     num//=10
# print(sum)
# num, sum = 12345, 0

# def find_sum(num, sum):
#     while num == 0:
#         return sum 
#     sum += num % 10
#     return find_sum(num//10, sum)
# print(find_sum(num, sum))  # Output: 15

# factorial
# def fact(num, i=1, res=1):
#     while i <= num:
#         res *= i
#         i+=1
#     return res
# print(fact(5))  # Output: 120

# def factorial(num,i=1,res=1):
#     if i > num:
#         return res
#     res*=i
#     return factorial(num,i+1,res)
# # print(factorial(5))  # Output: 120
# def fact(n):
#     if n<=1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))  # Output: 120
def sum_of(n):
    if n<=1:
        return 1
    return n+sum_of(n-1)
print(sum_of(9))