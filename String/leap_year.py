# import calendar
# year = int(input("Enter the year:"))
# if calendar.isleap(year):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

#  Using Lamda Function
leapyear =lambda year : (year %4 ==0 and year % 100!=0) or (year%400==0) 
year = int(input("Enter the number"))
if leapyear(year):
    print("leap year")
else:
    print("not leap year")
