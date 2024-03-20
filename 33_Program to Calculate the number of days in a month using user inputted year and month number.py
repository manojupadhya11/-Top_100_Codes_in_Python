#Program to calculate number of days in a month given user inputted year and month

year = int(input("Enter a Year "))
month  = int(input("Enter a Month in Number format "))

if ((month ==2) and ((year%4==0) or ((year%100 ==0) and (year%400 ==0)))):
    print("Number of days in this month is 29")
elif month == 2:
    print("Number of days in this month is 28")

elif((month == 1) or (month ==3) or (month == 5) or (month == 7) or (month == 8 ) or (month == 10) or (month == 12)):
    print("Number of days in this month is 31")
else:
    print("Number of days in month is 30")