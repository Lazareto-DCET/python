while True:
    try:
        x=int(input("Enter a number: "))
        print("The input is",x)
        break
    except:
        print("Invalid Input")
        print("Please enter a valid number.")
        
