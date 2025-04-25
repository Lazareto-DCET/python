while True:
    print("\n===================================")
    print("       SIMPLE BANKING SYSTEM       ")
    print("                by                 ")
    print("     Leandro Renee V. Lazareto     ")
    print("===================================")
    print("1. Deposit Funds")
    print("2. Withdraw Funds")
    print("3. Check Balance")
    print("4. Show Last Transaction")
    print("5. Exit")
    choice=input("\nEnter your choice: ")

    if (choice=="1"):
          while True:
              try:
                  d=float(input("\nEnter the amount to deposit: "))
                  print("Deposited", d, "pesos successfully")
                  break
              except:
                  print("Error input, try again")
                  
    elif (choice=="2"):
           while True:
               try:
                  w=float(input("\nEnter the amount to withdraw: "))
                  print("Withdrew", w, "pesos successfully")
                  break
               except:
                  print("Error input, try again")

    elif (choice=="3"):
        b=d-w
        print("Your balance is", b, "pesos")

    elif (choice=="4"):
        print("Last transaction: Withdrew", w, "pesos")

    elif (choice=="5"):
        print("Thank you for using this Simple Banking System :)")
        break

    else:
        print("Error input, try again")
        
                   
                  

          
    

    
