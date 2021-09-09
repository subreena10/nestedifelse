alphabet=input("enter a alphabet:")
integer=input("enter a integer:")
special_char=input("enter a special character:")
if alphabet=="A-Z" or alphabet=="a-z":
    if integer == "0-9":
        if special_char=="@,#,%":
            print("strong password")
        else:
            print("not a strong password.")
    else:
        print("invalid")
print(alphabet+special_char+integer)
            
