while True:
    print("\nWelcome to Mathing Operation")
    print("Start the program or Exit the program?")
    print("===================")
    print("[S]tart")
    print("[E]xit")
    print("===================")
    choice=input("Enter here: ")

    if (choice=="S" or choice=="s"):
        n1=float(input("Enter the first number: "))
        n2=float(input("Enter the second number: "))
        result=0;

        print("\n")
        print("===================")
        print("Choose an Operation")
        print("===================")
        print("[A]ddition")
        print("[S]ubtraction")
        print("[M]ultiplication")
        print("[D]ivision")
        print("-------------------")
        choice=input("Enter your choice: ")

        if (choice=="A" or choice=="a"):
            result=n1+n2
            print("\nThe sum is",result)
        elif (choice=="S" or choice=="s"):
            result=n1-n2
            print("\nThe difference is",result)
        elif (choice=="M" or choice=="m"):
            result=n1*n2
            print("\nThe product is",result)
        elif (choice=="D" or choice=="d"):
            if n2==0:
                print("\nIt cannot be divided into zero, sorry:(")
            else:
                result=n1/n2
                print("\nThe quotient is",result)
        else:
            print("\nInvalid Operation, try again!")
    elif (choice=="E" or choice=="e"):
        print("\nThank you for using this program<3")
        break
    else:
        print("Please enter the right input")

