print("Welcome to bank,insert ur card:")
total_amt=10000
card=input("enter a card:\n1)debit\n2)credit\n")
if card=="1" or card=="2":
    print("yes")
    language=input("choose a language:\n1)english\n2)hindi\n")
    if language=="1" or language=="2":
        print("yes")
        bank=input("choose a bank:\n1)saving bank account\n2)current bank account\n")
        if bank=="1" or bank=="2":
            print("yes")
            pin=int(input("enter ur pin:"))
            if pin >999 and pin<=9999:
                print("in process")
                transcation=input("choose a transcation:\n1)widrawal\n2)check balance\n")
                if transcation=="1":
                    print("loading")
                    amount=int(input("Enter a amount"))
                    if amount>0 and amount<=10000:
                        print("collect ur money")
                        amt=total_amt-amount
                        receipt=input("do u want a receipt:")
                        if receipt=="yes":
                            print( "collect ur receipt.This amount is left",amt)
                        else:
                            print("no.thank you for using bank.")
                    else:
                        print("enter a valid amount")
                else:
                    print("invalid transcation.please choose the correct the transcation.")
            else:
                print("incorrect pin.please try again")
        else:
            print("please choose the correct bank")
    else:
        print("choose a correct language.")
else:
    print("ok")            

