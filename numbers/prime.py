# # # num = int(input("Enter the number:"))
# # # flag = 0
# # # if num < 2:
# # #     flag = 1
# # # for i in range(2, num):
# # #     if num % i == 0:
# # #         flag = 1
# # #         break
# # # if flag == 1:
# # #     print(num, "is not a prime number")
# # # else:
# # #     print(num,"is prime")

# # num = int(input("Enter the number:"))
# # flag = 0
# # if num < 2:
# #     flag = 1
# # else:
# #     for i in range(3, int(pow(num,0.5)+1),2):
# #         if num % i == 0:
# #             flag = 1
# #             break
# # if flag == 0:
# #     print(num,"is prime")
# # else:
# #     print(num,"is not prime")  
# # num = int(input("ENTER THE NUMBER"))
# # def check_prime(num, iter = 2):
# #     if num == iter:
# #         return True
# #     if num % iter == 0:
# #         return False
# #     if num <2:
# #         return False
# #     return check_prime(num, iter + 1)
# # if check_prime(num) ==True:
# #     print("Prime")
# # else:
# #     print("Not prime")   # 2 3 5 7 11 13


# num1= int(input("Enter the number: "))
# num2 = int(input("Enter the number: "))
# out = []
# for i in range(num1,num2+1):
#     flag = 0
#     if i < 2:
#         continue
#     for j in range(2, i):
#         if i % j == 0:
#             flag = 1
#             break
#     if flag == 0:
#         out.append(i)
# print(out)
        

def check_prime(num, iter =2):
    if num == iter:
        return True
    if num % iter == 0:
        return False
    if num < 2:
        return False
    return check_prime(num, iter + 1)

out = []
def prime(num1,num2):
    for num in range(num1, num2+1):
        if check_prime(num) == True:
            out.append(num)
    return out

print(prime(int(input()),int(input())))