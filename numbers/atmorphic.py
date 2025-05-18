def atmorphic(num):
    square =pow(num,2)
    mod=pow(10,len(str(num)))
    if square%mod==num:
        return True
    else:
        return False
print(atmorphic(int(input("Enter the number:"))))