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
    
def main():
    print("\nWelcome to Conversion Menu")
    while True:
        print("=======")
        print("[S]tart")
        print("[E]xit")
        print("=======")
        choice=input("Select one: ")

        if (choice=="S" or choice=="s"):
            conversion()

        elif (choice=="E" or choice=="e"):
            print("\nThank you for using this program :)")
            break
        else:
            print("\nInvalid input, try again")

def conversion():
    while True:
        print("\n=============")
        print("[P]hysics")
        print("[T]emperature")
        print("[L]ength")
        print("[B]ack")
        print("=============")
        choice=input("Select one: ")

        if (choice=="T" or choice=="t"):
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
                choice=input("Select one: ")

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
        elif (choice=="L" or choice=="l"):
            length()
        elif (choice=="P" or choice=="p"):
            physics()
        elif (choice=="B" or choice=="b"):
            break
        else:
            print("\nInvalid input, try again")

def length():
    while True:
        print("Pick a Length Convertion")
        print("=============================")
        print("Choose one")
        print("1. Meter")
        print("2. Centimeter")
        print("3. Kilometer")
        print("4. Mile")
        print("5. Yard")
        print("6. Inch")
        print("7. Foot")
        print("8. Back")
        print("=============================")
        choice=input("Select one: ")

        if choice.lower() == "1":
            while True:
                print("\nInto what unit?")
                print("===============")
                print("Choose one")
                print("1. Centimeter")
                print("2. Kilometer")
                print("3. Mile")
                print("4. Yard")
                print("5. Inch")
                print("6. Foot")
                print("7. Back")
                print("===============")
                choice=input("Pick one: ")
                
                if choice.lower()=="1":
                    while True:
                        try:
                            meter = int(input("Enter Meter amount: "))
                            mtocm = meter*100
                            print("Answer is ", mtocm, "cm")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="2":
                    while True:
                        try:
                            meter = int(input("Enter Meter amount: "))
                            mtokm = meter/1000
                            print("Answer is ", mtokm, "km")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="3":
                    while True:
                        try:
                            meter = int(input("Enter Meter amount: "))
                            mtomi = meter/1609
                            print("Answer is ", mtomi, "mi")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="4":
                    while True:
                        try: 
                            meter = int(input("Enter Meter amount: "))
                            mtoyd = meter*1.094
                            print("Answer is ", mtoyd, "yd")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="5":
                    while True:
                        try:
                            meter = int(input("Enter Meter amount: "))
                            mtoin = meter*39.37
                            print("Answer is ", mtoin, "in")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="6":
                    while True:
                        try:
                            meter = int(input("Enter Meter amount: "))
                            mtoft = meter*3.281
                            print("Answer is ", mtoft, "ft")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")
                
                elif choice.lower()=="7":
                    break
                    
                else:
                    print("\nInvalid input, try again")

        elif choice.lower() == "2":
            while True:
                print("\nInto what unit?")
                print("===============")
                print("Choose one")
                print("1. Meter")
                print("2. Kilometer")
                print("3. Mile")
                print("4. Yard")
                print("5. Inch")
                print("6. Foot")
                print("7. Back")
                print("===============")
                choice=input("Pick one: ")

                if choice.lower()=="1":
                    while True:
                        try:
                            centimeter = int(input("Enter Centieter amount: "))
                            cmtom = centimeter/100
                            print("Answer is ", cmtom, "cm")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="2":
                    while True:
                        try:                       
                            centimeter = int(input("Enter Centimeter amount: "))
                            cmtokm = centimeter/100000
                            print("Answer is ", cmtokm, "km")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="3":
                    while True:
                        try:
                            centimeter = int(input("Enter Centimeter amount: "))
                            cmtomi = centimeter/160900
                            print("Answer is ", cmtomi, "mi")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="4":
                    while True:
                        try:
                            centimeter = int(input("Enter Centimeter amount: "))
                            cmtoyd = centimeter/91.44
                            print("Answer is ", cmtoyd, "yd")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="5":
                    while True:
                        try:
                            centimeter = int(input("Enter Centimeter amount: "))
                            cmtoin = centimeter/2.54
                            print("Answer is ", cmtoin, "in")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="6":
                    while True:
                        try:
                            centimeter = int(input("Enter Centimeter amount: "))
                            cmtoft = centimeter/30.48
                            print("Answer is ", cmtoft, "ft")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="7":
                    break
                    
                else:
                    print("\nInvalid input, try again")

        elif choice.lower() == "3":
            while True:
                print("\nInto what unit?")
                print("===============")
                print("Choose one")
                print("1. Meter")
                print("2. Centimeter")
                print("3. Mile")
                print("4. Yard")
                print("5. Inch")
                print("6. Foot")
                print("7. Back")
                print("===============")
                choice=input("Pick one: ")
                
                if choice.lower()=="1":
                    while True:
                        try:
                            kilometer = int(input("Enter Centieter amount: "))
                            kmtom = kilometer*1000
                            print("Answer is ", kmtom, "m")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="2":
                    while True:
                        try:
                            kilometer = int(input("Enter Centimeter amount: "))
                            kmtocm = kilometer*100000
                            print("Answer is ", kmtocm, "cm")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="3":
                    while True:
                        try:
                            kilometer = int(input("Enter Centimeter amount: "))
                            kmtomi = kilometer/1.609
                            print("Answer is ", kmtomi, "mi")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="4":
                    while True:
                        try:
                            kilometer = int(input("Enter Centimeter amount: "))
                            kmtoyd = kilometer*1094
                            print("Answer is ", kmtoyd, "yd")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="5":
                    while True:
                        try:
                            kilometer = int(input("Enter Centimeter amount: "))
                            kmtoin = kilometer*39370
                            print("Answer is ", kmtoin, "in")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="6":
                    while True:
                        try:
                            kilometer = int(input("Enter Centimeter amount: "))
                            kmtoft = kilometer*3281
                            print("Answer is ", kmtoft, "ft")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="7":
                    break
                    
                else:
                    print("\nInvalid input, try again")
            
        elif choice.lower() == "4":
            while True:
                print("\nInto what unit?")
                print("===============")
                print("Choose one")
                print("1. Meter")
                print("2. Centimeter")
                print("3. Kilometer")
                print("4. Yard")
                print("5. Inch")
                print("6. Foot")
                print("7. Back")
                print("===============")
                choice=input("Pick one: ")
                
                if choice.lower()=="1":
                    while True:
                        try:
                            mile = int(input("Enter Centieter amount: "))
                            mitom = mile*1609
                            print("Answer is ", mitom, "m")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="2":
                    while True:
                        try:
                            mile = int(input("Enter Centimeter amount: "))
                            mitocm = mile*160900
                            print("Answer is ", mitocm, "cm")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="3":
                    while True:
                        try:
                            mile = int(input("Enter Centimeter amount: "))
                            mitokm = mile*1.609
                            print("Answer is ", mitokm, "km")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="4":
                    while True:
                        try:
                            mile = int(input("Enter Centimeter amount: "))
                            mitoyd = mile*1760
                            print("Answer is ", mitoyd, "yd")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="5":
                    while True:
                        try:
                            mile = int(input("Enter Centimeter amount: "))
                            mitoin = mile*63360
                            print("Answer is ", mitoin, "in")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="6":
                    while True:
                        try:
                            mile = int(input("Enter Centimeter amount: "))
                            mitoft = mile*5280
                            print("Answer is ", mitoft, "ft")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="7":
                    break
                    
                else:
                    print("\nInvalid input, try again")
            
        elif choice.lower() == "5":
            while True:
                print("\nInto what unit?")
                print("===============")
                print("Choose one")
                print("1. Meter")
                print("2. Centimeter")
                print("3. Kilometer")
                print("4. Mile")
                print("5. Inch")
                print("6. Foot")
                print("7. Back")
                print("===============")
                choice=input("Pick one: ")
                

                if choice.lower()=="1":
                    print("Meter = inch/39.37")
                    while True:
                        try:
                            yard = int(input("Enter Centieter amount: "))
                            ydtom = yard/1.094
                            print("Answer is ", ydtom, "m")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="2":
                    print("Centimeter = inch/39.37")
                    while True:
                        try:
                            yard = int(input("Enter Centimeter amount: "))
                            ydtocm = yard*91.44
                            print("Answer is ", ydtocm, "cm")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="3":
                    while True:
                        try:
                            print("Meter = inch/39.37")
                            yard = int(input("Enter Centimeter amount: "))
                            ydtokm = yard/1094
                            print("Answer is ", ydtokm, "km")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="4":
                    print("Meter = inch/39.37")
                    while True:
                        try:
                            yard = int(input("Enter Centimeter amount: "))
                            ydtomi = yard/1760
                            print("Answer is ", ydtomi, "mi")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="5":
                    print("Meter = inch/39.37")
                    while True:
                        try:
                            yard = int(input("Enter Centimeter amount: "))
                            ydtoin = yard*36
                            print("Answer is ", ydtoin, "in")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="6":
                    print("Meter = inch/39.37")
                    while True:
                        try:
                            yard = int(input("Enter Centimeter amount: "))
                            ydtoft = yard*3
                            print("Answer is ", ydtoft, "ft")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="7":
                    break
                    
                else:
                    print("\nInvalid input, try again")
            
        elif choice.lower() == "6":
            while True:
                print("\nInto what unit?")
                print("===============")
                print("Choose one")
                print("1.Meter")
                print("2. Centimeter")
                print("3. Kilometer")
                print("4. Mile")
                print("5. Yard")
                print("6. Foot")
                print("7. Back")
                print("===============")
                choice=input("Pick one: ")

                if choice.lower()=="1":
                    print("Meter = inch/39.37")
                    while True:
                        try:
                            inch = int(input("Enter Centieter amount: "))
                            intom = inch/39.37
                            print("Answer is ", intom, "m")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="2":
                    print("Centimeter = inch*2.54")
                    while True:
                        try:
                            inch = int(input("Enter Centimeter amount: "))
                            intocm = inch*2.54
                            print("Answer is ", intocm, "cm")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="3":
                    print("Kilometer = inch/39370")
                    while True:
                        try:
                            inch = int(input("Enter Centimeter amount: "))
                            intokm = inch/39370
                            print("Answer is ", intokm, "km")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="4":
                    print("Mile = inch/63360")
                    while True:
                        try: 
                            inch = int(input("Enter Centimeter amount: "))
                            intomi = inch/63360
                            print("Answer is ", intomi, "mi")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="5":
                    print("Yard = inch/36")
                    while True:
                        try:
                            inch = int(input("Enter Centimeter amount: "))
                            intoyd = inch/36
                            print("Answer is ", intoyd, "yd")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="6":
                    print("Foot = inch/12")
                    while True:
                        try:
                            inch = int(input("Enter Centimeter amount: "))
                            intoft = inch/12
                            print("Answer is ", intoft, "ft")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="7":
                    break
                    
                else:
                    print("\nInvalid input, try again")

        elif choice.lower() == "7":
            while True:
                print("\nInto what unit?")
                print("===============")
                print("Choose one")
                print("1. Meter")
                print("2. Centimeter")
                print("3. Kilometer")
                print("4. Mile")
                print("5. Yard")
                print("6. Inch")
                print("7. Back")
                print("===============")
                choice=input("Pick one: ")

                if choice.lower()=="1":
                    print("Meter = foot/3.281")
                    while True:
                        try:
                            foot = int(input("Enter Centieter amount: "))
                            fttom = foot/3.281
                            print("Answer is ", fttom, "m")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="2":
                    print("Centimeter = foot*30.48")
                    while True:
                        try:
                            foot = int(input("Enter Centimeter amount: "))
                            fttocm = foot*30.48
                            print("Answer is ", fttocm, "cm")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="3":
                    print("Kilometer = foot/3281")
                    while True:
                        try:
                            foot = int(input("Enter Centimeter amount: "))
                            fttokm = foot/3281
                            print("Answer is ", fttokm, "km")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="4":
                    print("Mile = foot/5280")
                    while True:
                        try:
                            foot = int(input("Enter Centimeter amount: "))
                            fttomi = foot/5280
                            print("Answer is ", fttomi, "mi")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="5":
                    print("Yard = foot/3")
                    while True:
                        try:
                            foot = int(input("Enter Centimeter amount: "))
                            fttoyd = foot/3
                            print("Answer is ", fttoyd, "yd")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="6":
                    print("Inch = foot*12")
                    while True:
                        try:
                            foot = int(input("Enter Centimeter amount: "))
                            fttoin = foot*12
                            print("Answer is ", fttoin, "in")
                            break
                        except ValueError:
                            print("\nYou just entered a letter, try again")

                elif choice.lower()=="7":
                    break
                    
                else:
                    print("\nInvalid input, try again")
        elif choice.lower()=="8":
            break
        else:
            print("\nInvalid input, try again")

def physics():
    while True:
            print("\n=======================")
            print("[S]peed")
            print("[F]orce")
            print("[T]ime")
            print("[V]oltage to Horsepower")
            print("[H]orsepower to Voltage")
            print("[B]ack")
            print("=======================")
            choice = input("Enter your choice: ")
            
            if (choice=="S" or choice=="s"):
                print("S = Distance / Time")
                while True:
                    try:
                        d = float(input("Enter Distance (m): "))
                        t = float(input("Enter Time (s): "))
                        print("Speed:", d, "/", t,)
                        if t == 0:
                            print("Invalid Time! Cannot divide by zero.")
                            break
                        else:
                            print("Speed =", d / t, "m/s")
                            break
                    except ValueError:
                        print("Invalid Input!!!")
            elif (choice=="F" or choice=="f"):
                while True:
                    try:
                        print("Force = Mass * Acceleration")
                        m = float(input("Enter Mass (kg): "))
                        a = float(input("Enter Acceleration (m/s^2): "))
                        print("Force =", m, "*", a,)
                        print("Force =", m * a, "n")
                        
                        break
                    except ValueError:
                        print("Invalid Input!!!")
            elif (choice=="T" or choice=="t"):
                print("Time = Distance / velocity")
                while True:
                    try:
                        d = float(input("Enter Distance (m): "))
                        v = float(input("Enter Velocity (m/s): "))
                        print("Time =", d ,"/", v,)
                        if v == 0:
                            print("Invalid Time! Cannot divide by zero.")
                            break
                        else:
                            print("Time =", dp / v, "s")
                            break
                    except ValueError:
                        print("Invalid Input!!!")           

            elif (choice=="V" or choice=="v"):
                print("HP = (V * I * efficiency) / 746")
                while True:
                    try:
                        V = float(input("Enter Voltage (V): "))
                        I = float(input("Enter Current (A): "))
                        efficiency = float(input("Enter Efficiency (as decimal): "))
                        power_watts = V * I * efficiency
                        horsepower = power_watts / 746
                        print("Power = ", V,"*", I,"*", efficiency)
                        print("Power =", horsepower,"HP")
                        break
                    except ValueError:
                        print("Invalid Input!!!")
           
           
            elif (choice=="H" or choice=="h"):
                 print("HP = (V * I * efficiency) / 746")
                 while True:  
                    try:
                        V = float(input("Enter Voltage (V): "))
                        I = float(input("Enter Current (A): "))
                        efficiency = float(input("Enter Efficiency (as decimal): "))
                        power_watts =  V* 746
                        voltage = power_watts / (I * efficiency)
                        print("volatge = ", V,"*", I,"*", efficiency)
                        print("voltage =", voltage, "V")
                        break 
                    except ValueError:
                        print("Invalid Input!!!")
                        
            elif (choice=="B" or choice=="b"):
                break
            else: 
                print("Invalid Choice!")

if __name__ == "__main__":
    main()   
