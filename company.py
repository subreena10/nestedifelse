age=int(input("enter ur age:"))
sex=input("enter 'F','M':")
marital_status=input("married 'Y', 'N':")
if sex=='F':
    print("she will work only in urban areas.")
elif sex=='M' and age>=20 or age<=40:
        print("he will work only in urban areas.")
else:
    if sex=='M' and age>=40 and age<=60:
        print("he will work only in urban areas.")
    else:
        print("invalid data")




