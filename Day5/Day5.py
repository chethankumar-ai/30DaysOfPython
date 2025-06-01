def result(list):
    sum=0
    count=0
    for i in list:
        if type(i)==int:
            sum+=i
            count+=1
    print("sum of values",sum)
    if count>0:
        print("Average",sum/count)
    
    
x=eval(input("Enter the list of values"))
print(result(x))
