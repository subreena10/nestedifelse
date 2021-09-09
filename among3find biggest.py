first=int(input("enter a number:"))
second=int(input("enter a number:"))
third=int(input("enter a number:"))
if first>second:
    if first>third:
        print("first is largest number")
    else:
        print("third is largest number")
elif second>third:
    print("second is largest number")
else:
    print("third is largest")