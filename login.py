print("***Welcome to my login page***")
username1="saab121"
password1="sa10bu"
username2=input("Enter ur username:")
password2=input("enter ur password:")
if username2==username1 and password2==password1:
    print("login successfully.")
    if username2!=username1:
        print("username not matching")
    else:
        print("try again.")
elif username2!=username1 and password2!=password1: 
    print("invalid password and username.")
    print("create new account:")
    usern=input("enter ur name:")
    print("your username is",usern)
    passwd=input("enter a password:") 
    re_passwd=input("enter ur password again:")
    if passwd==re_passwd:
        print("your passwd is matching. Your new account is successfully created.")
    else:
            print("password not matching. try again.")
else:
    print("sorry!try again.")




 