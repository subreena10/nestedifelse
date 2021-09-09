print("***welcome to question and answere game***")
question=input("May i ask u  a question:")
if question=="yes":
    print("let's start")
    name=input("what is your name ?")
    if name=="sabreena":
        print("your answere is right.")
        age=input("how old you are? ")
        if age=="20":
            print("Correct")
            place=input("where do u live? ")
            if place=="kashmir":
                print("Righr answere")
                hobby=input("What is your hobby? ")
                if hobby=="writing":
                    print("Answere is correct")
                else:
                    print("invalid hobby")
            else:
                print("wrong place")
        else:
            print("invalid age")
    else:
        print("name is not correct.")
else:
    print("no")