import math 
def is_perfect_square(n):
    if n<0:
        return False
    root = int(math.sqrt(n))
    if root*root == n:
        return True
    else:
        return False
# Test the function
n = int(input("Enter a number: "))
if is_perfect_square(n):
    print(f"{n} is a perfect square.")
else:   
    print(f"{n} is not a perfect square.")
    