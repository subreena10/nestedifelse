year=int(input("enter a year:"))
if year%100==0:
    if year%400==0:
        print("year is a leap")
    else:
        print("year is not a leap",year)    
else:
    if year%4==0:
        print("leap year")
    else:
        print("not leap year")