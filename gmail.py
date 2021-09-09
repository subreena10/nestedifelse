print("***Welcome to gmail***")
name=input("Enter ur name:- ")
if name=="saab":
    print("correct name. you can access ur account")
    mail_id=input("Enter ur mail id:- ")
    if mail_id=="abcdefghij122@gmail.com":
        print("loading")
        passwrd=input("enter ur password:-")
        if passwrd=="sab123@":
            print("matching.correct password")
            contact_num=int(input("enter ur phone number:-"))
            if contact_num==1234567890:
                print("successfully login...")
            else:
                print("not found any account.")
        else:
            print("not matching password")
    else:
        print("invalid mail id.")
else:
    print("not found.")