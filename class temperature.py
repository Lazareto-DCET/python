class degree:
    def __init__(self,k=0,f=0,c=0):
        self.vark=k
        self.varf=f
        self.varc=c

    def setVarK(self,k):
        self.vark=k

    def setVarF(self,f):
        self.varf=f

    def setVarC(self,c):
        self.varc=c
        
    def getc_to_f(self):
        self.c_to_f=self.varc*(9/5)+32
        return self.c_to_f

    def getc_to_k(self):
        self.c_to_k=self.varc+273.15
        return self.c_to_k

    def getf_to_c(self):
        self.f_to_c=(self.varf-32)*5/9
        return self.f_to_c

    def getf_to_k(self):
        self.f_to_k=(self.varf-32)*5/9+273.15
        return self.f_to_k

    def getk_to_c(self):
        self.k_to_c=self.vark-273.15
        return self.k_to_c

    def getk_to_f(self):
        self.k_to_f=(self.vark-273.15)*9/5+32
        return self.k_to_f
    
print("\nWelcome to Temperature converter")
while True:
    print("\nTemperature Converter")
    print("=======")
    print("[S]tart")
    print("[E]xit")
    print("=======")
    choice=input("Select one: ")

    if (choice=="S" or choice=="s"):
        print("\nConvert a temperature into a following")
        while True:
            print("\n============================================")
            print("1. Celsius to Fahrenheit    1°C = 33.8°F ")
            print("2. Celsius to Kelvin        1°C = 274.15°K")
            print("3. Fahrenheit to Celsius    1°F = -17.22°C")
            print("4. Fahrenheit to Kelvin     1°F = 255.93°K")
            print("5. Kelvin to Celsius        1°K = -272.15°C")
            print("6. Kelvin to Fahrenheit     1°K = -457.87°F")
            print("\n7. Back")
            print("============================================")
            choice=input("Choose one: ")

            if (choice=="1"):
                print("\nFormula: F = C * (9/5) + 32")
                while True:
                    try:
                        cf=degree()
                        c=float(input("\nEnter the temp: "))
                        cf.setVarC(c)
                        f=cf.getc_to_f()
                        print("F =", c,"* (9/5) + 32")
                        print("\nConverted that", c,"°C is", round(f,2), "°F")
                        break
                    except ValueError:
                        print("\nInvalid input, try again")
                        
            elif (choice=="2"):
                print("\nFormula: K = C + 273.15")
                while True:
                    try:
                        ck=degree()
                        c=float(input("\nEnter the temp: "))
                        ck.setVarC(c)
                        k=ck.getc_to_k()
                        print("K =", c,"+ 273.15")
                        print("\nConverted that", c,"°C is", round(k,2), "°K")
                        break
                    except ValueError:
                        print("\nInvalid input, try again")
                        
            elif (choice=="3"):
                print("\nFormula: C = (F - 32) * 5/9")
                while True:
                    try:
                        fc=degree()
                        f=float(input("\nEnter the temp: "))
                        fc.setVarF(f)
                        c=fc.getf_to_c()
                        print("C = (",f,"- 32 ) * 5/9")
                        print("\nConverted that", f,"°F is", round(c,2), "°C")
                        break
                    except ValueError:
                        print("\nInvalid input, try again")
                        
                        
            elif (choice=="4"):
                print("\nFormula: K = (F - 32) * 5/9 + 273.15")
                while True:
                    try:
                        fk=degree()
                        f=float(input("\nEnter the temp: "))
                        fk.setVarF(f)
                        k=fk.getf_to_k()
                        print("K = (",f,"- 32 ) * 5/9 + 273.15")
                        print("\nConverted that", f,"°F is", round(k,2), "°K")
                        break
                    except ValueError:
                        print("\nInvalid input, try again")
                        
            elif (choice=="5"):
               print("\nFormula: C = K - 273.15")
               while True:
                    try:
                        kc=degree()
                        k=float(input("\nEnter the temp: "))
                        kc.setVarK(k)
                        c=kc.getk_to_c()
                        print("C =",k,"- 273.15")
                        print("\nConverted that", k,"°K is", round(c,2), "°C")
                        break
                    except ValueError:
                        print("\nInvalid input, try again")
            
            elif (choice=="6"):
                print("\nFormula: F = (K - 32) * 5/9 + 32")
                while True:
                    try:
                        kf=degree()
                        k=float(input("\nEnter the temp: "))
                        kf.setVarK(k)
                        f=kf.getk_to_f()
                        print("F = (",k,"- 32 ) * 5/9 + 32")
                        print("\nConverted that", k,"°K is", round(f,2), "°F")
                        break
                    except ValueError:
                        print("\nInvalid input, try again")
            elif (choice=="7"):
                break
            else:
                print("\nInvalid input! Please select a valid unit.")


    elif (choice=="E" or choice=="e"):
        print("\nThank you for using this program :)")
        break
    else:
        print("\nInvalid input, try again")

