while True:
    print("\n===================")
    print("Choose an Operation")
    print("===================")
    print("[A]ddition")
    print("[S]ubtraction")
    print("[M]ultiplication")
    print("[D]ivision")
    print("[E]xit")
    print("-------------------")
    choice=input("Enter your choice: ")
    
    if (choice=="A" or choice=="a"):
        try:
            n1=float(input("\nEnter the first number: "))
            n2=float(input("Enter the second number: "))
            result=n1+n2
            print(n1,"+",n2,"=",result)
        except:
            print("\nYou just entered a letter, try again")
            
    elif (choice=="S" or choice=="s"):
        try:
            n1=float(input("\nEnter the first number: "))
            n2=float(input("Enter the second number: "))
            result=n1-n2
            print(n1,"-",n2,"=",result)
        except:
            print("\nYou just entered a letter, try again")

    elif (choice=="M" or choice=="m"):
        try:
            n1=float(input("\nEnter the first number: "))
            n2=float(input("Enter the second number: "))
            result=n1*n2
            print(n1,"*",n2,"=",result)
        except:
            print("\nYou just entered a letter, try again")
                
    elif (choice=="D" or choice=="d"):
        try:
            n1=float(input("\nEnter the first number: "))
            n2=float(input("Enter the second number: "))
            if n1==0:
                print("\nIt cannot be divided into zero, sorry :(")
            elif n2==0:
                print("\nIt cannot be divided into zero, sorry :(")
            else:
                result=n1/n2
                print(n1,"/",n2,"=",result)
        except:
            print("\nYou just entered a letter, try again")
            
    elif (choice=="E" or choice=="e"):
        print("\nThank you for using this program :)")
        break
    
    else:
        print("\nInvalid operation, try again")
                

