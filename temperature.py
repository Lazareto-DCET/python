def main():
    print("\nWelcome to Temperature converter")
    while True:
        print("\nTemperature Converter")
        print("=======")
        print("[S]tart")
        print("[E]xit")
        print("=======")
        choice=input("Select one: ")

        if (choice=="S" or choice=="s"):
            temperature()

        elif (choice=="E" or choice=="e"):
            print("\nThank you for using this program :)")
            break
        else:
            print("\nInvalid input, try again")

def temperature():
    print("\nConvert a temperature into a following")
    while True:
        print("\n============================================")
        print("1. Celsius to Fahrenheit    1°C = 33.8°F ")
        print("2. Celsius to Kelvin        1°C = 274.15°K")
        print("3. Fahrenheit to Celsius    1°F = -17.2222°C")
        print("4. Fahrenheit to Kelvin     1°F = 255.928°K")
        print("5. Kelvin to Celsius        1°K = -272.15°C")
        print("6. Kelvin to Fahrenheit     1°K = -457.87°F")
        print("\n7. Back")
        print("============================================")
        choice=input("Choose one: ")

        if (choice=="1"):
            c_to_f_convert()
        elif (choice=="2"):
            c_to_k_convert()
        elif (choice=="3"):
            f_to_c_convert()
        elif (choice=="4"):
            f_to_k_convert()
        elif (choice=="5"):
            k_to_c_convert()
        elif (choice=="6"):
            k_to_f_convert()
        elif (choice=="7"):
            break
        else:
            print("\nInvalid input! Please select a valid unit.")

def c_to_f_convert():
    print("\nFormula: F = C * (9/5) + 32")
    while True:
        try:
            k=float(input("\nEnter the temp: "))
            result=k*(9/5)+32
            print("F =", k,"* (9/5) + 32")
            print("\nConverted that", k,"°C is", round(result,2), "°F")
            break
        except ValueError:
            print("\nYou just entered a letter, try again")
            
def c_to_k_convert():
    print("\nFormula: K = C + 273.15")
    while True:
        try:
            k=float(input("\nEnter the temp: "))
            result=k+273.15
            print("K =", k,"+ 273.15")
            print("\nConverted that", k,"°C is", round(result,2), "°K")
            break
        except ValueError:
            print("\nYou just entered a letter, try again")
            
def f_to_c_convert():
    print("\nFormula: C = (F - 32) * 5/9")
    while True:
        try:
            k=float(input("\nEnter the temp: "))
            result=(k-32)*5/9
            print("C = (",k,"- 32 ) * 5/9")
            print("\nConverted that", k,"°F is", round(result,2), "°C")
            break
        except ValueError:
            print("\nYou just entered a letter, try again")
            
def f_to_k_convert():
    print("\nFormula: K = (F - 32) * 5/9 + 273.15")
    while True:
        try:
            k=float(input("\nEnter the temp: "))
            result=(k-32)*5/9+273.15
            print("K = (",k,"- 32 ) * 5/9 + 273.15")
            print("\nConverted that", k,"°F is", round(result,2), "°K")
            break
        except ValueError:
            print("\nYou just entered a letter, try again")
            
def k_to_c_convert():
    print("\nFormula: C = K - 273.15")
    while True:
        try:
            k=float(input("\nEnter the temp: "))
            result=k-273.15
            print("C =",k,"- 273.15")
            print("\nConverted that", k,"°K is", round(result,2), "°C")
            break
        except ValueError:
            print("\nYou just entered a letter, try again")
            
def k_to_f_convert():
    print("\nFormula: F = (K - 32) * 5/9 + 32")
    while True:
        try:
            k=float(input("\nEnter the temp: "))
            result=(k-273.15)*9/5+32
            print("F = (",k,"- 32 ) * 5/9 + 32")
            print("\nConverted that", k,"°K is", round(result,2), "°F")
            break
        except ValueError:
            print("\nYou just entered a letter, try again")
            
if __name__ == "__main__":
    main()           
   

