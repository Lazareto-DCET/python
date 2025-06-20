while True:
    print("========================")
    print("Multi-Subject Calculator")
    print("========================")
    print("[P] Physics")
    print("[L] Length")
    print("[T] Temperature")
    print("[X] Exit")
    print("------------------------")
    main_choice = input("Enter your choice: ").upper()
#JENZ's PART
    if main_choice == 'P':
        while True:
            print("========================")
            print("Physics Calculator")
            print("========================")
            print("[S]peed")
            print("[F]orce")
            print("[T]ime")
            print("[V]oltage to Horsepower")
            print("[H]orsepower to Voltage")
            print("[B]ack")
            choice = input("Enter your choice: ").upper()
            
            if choice == 'S':
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
            elif choice == 'F':
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
            elif choice == 'T':
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

            elif choice == 'V':
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
           
           
            elif choice == 'H':
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
                        
            elif choice == 'B':
                break
            else: 
                print("Invalid Choice!")
#AIRO'S PART                 
    elif main_choice == 'L':
        while True:
            print("Pick a Length Convertion")
            print("=============================")
            print("Choose one")
            print("[M]Meter")
            print("[Cm]Centimeter")
            print("[Km]Kilometer")
            print("[Mi]Mile")
            print("[Yd]Yard")
            print("[In]Inch")
            print("[Ft]Foot")
            print("[B]ack")
            print("=============================")
            choice=input("Select one: ")

            if choice.lower() == "m":
                print("\nInto what unit?")
                print("===============")
                print("Choose one")
                print("[Cm]Centimeter")
                print("[Km]Kilometer")
                print("[Mi]Mile")
                print("[Yd]Yard")
                print("[In]Inch")
                print("[Ft]Foot")
                print("[B]ack")
                print("===============")
                choice=input("Pick one: ")
                
                if choice.lower()=="cm":
                    print("Centimeter = meter*100")
                    meter = int(input("Enter Meter amount: "))
                    mtocm = meter*100
                    print("Answer is ", mtocm, "cm")

                elif choice.lower()=="km":
                    print("Kilometer = meter/1000")
                    meter = int(input("Enter Meter amount: "))
                    mtokm = meter/1000
                    print("Answer is ", mtokm, "km")

                elif choice.lower()=="mi":
                    print("Mile = meter/1609")
                    meter = int(input("Enter Meter amount: "))
                    mtomi = meter/1609
                    print("Answer is ", mtomi, "mi")

                elif choice.lower()=="yd":
                    print("Yard = meter*1.094")
                    meter = int(input("Enter Meter amount: "))
                    mtoyd = meter*1.094
                    print("Answer is ", mtoyd, "yd")

                elif choice.lower()=="in":
                    print("Inch = meter*39.37")
                    meter = int(input("Enter Meter amount: "))
                    mtoin = meter*39.37
                    print("Answer is ", mtoin, "in")

                elif choice.lower()=="ft":
                    print("Foot = meter*3.281")
                    meter = int(input("Enter Meter amount: "))
                    mtoft = meter*3.281
                    print("Answer is ", mtoft, "ft")
                elif choice.lower()== 'b':
                    break
                else:
                    print("\nInvalid input, try again")

            elif choice.lower() == "cm":
                print("\nInto what unit?")
                print("===============")
                print("Choose one")
                print("[M]Meter")
                print("[Km]Kilometer")
                print("[Mi]Mile")
                print("[Yd]Yard")
                print("[In]Inch")
                print("[Ft]Foot")
                print("[B]ack")
                print("===============")
                choice=input("Pick one: ")

                if choice.lower()=="m":
                    print("Meter = Centimeter/100")
                    centimeter = int(input("Enter Centieter amount: "))
                    cmtom = centimeter/100
                    print("Answer is ", cmtom, "cm")

                elif choice.lower()=="km":
                    print("Kilometer = Centimeter/100000")
                    centimeter = int(input("Enter Centimeter amount: "))
                    cmtokm = centimeter/100000
                    print("Answer is ", cmtokm, "km")

                elif choice.lower()=="mi":
                    print("Mile = Centimeter/160900")
                    centimeter = int(input("Enter Centimeter amount: "))
                    cmtomi = centimeter/160900
                    print("Answer is ", cmtomi, "mi")

                elif choice.lower()=="yd":
                    print("Yard = Centimeter/91.44")
                    centimeter = int(input("Enter Centimeter amount: "))
                    cmtoyd = centimeter/91.44
                    print("Answer is ", cmtoyd, "yd")

                elif choice.lower()=="in":
                    print("Inch = Centimeter/2.54")
                    centimeter = int(input("Enter Centimeter amount: "))
                    cmtoin = centimeter/2.54
                    print("Answer is ", cmtoin, "in")

                elif choice.lower()=="ft":
                    print("Foot = Centimeter/30.48")
                    centimeter = int(input("Enter Centimeter amount: "))
                    cmtoft = centimeter/30.48
                    print("Answer is ", cmtoft, "ft")
                elif choice.lower()== 'b':
                    break                    
                else:
                    print("\nInvalid input, try again")

            elif choice.lower() == "km":
                print("\nInto what unit?")
                print("===============")
                print("Choose one")
                print("[M]Meter")
                print("[Cm]Centimeter")
                print("[Mi]Mile")
                print("[Yd]Yard")
                print("[In]Inch")
                print("[Ft]Foot")
                print("[B]ack")
                print("===============")
                choice=input("Pick one: ")
                
                if choice.lower()=="m":
                    print("Meter = Kilometer*1000")
                    kilometer = int(input("Enter Centieter amount: "))
                    kmtom = kilometer*1000
                    print("Answer is ", kmtom, "m")

                elif choice.lower()=="cm":
                    print("Centimeter = Kilometer*100000")
                    kilometer = int(input("Enter Centimeter amount: "))
                    kmtocm = kilometer*100000
                    print("Answer is ", kmtocm, "cm")

                elif choice.lower()=="mi":
                    print("Mile = Kilometer/1.609")
                    kilometer = int(input("Enter Centimeter amount: "))
                    kmtomi = kilometer/1.609
                    print("Answer is ", kmtomi, "mi")

                elif choice.lower()=="yd":
                    print("Yard = Kilometer*1094")
                    kilometer = int(input("Enter Centimeter amount: "))
                    kmtoyd = kilometer*1094
                    print("Answer is ", kmtoyd, "yd")

                elif choice.lower()=="in":
                    print("Inch = Kilometer*39370")
                    kilometer = int(input("Enter Centimeter amount: "))
                    kmtoin = kilometer*39370
                    print("Answer is ", kmtoin, "in")

                elif choice.lower()=="ft":
                    print("Foot = Kilometer*3281")
                    kilometer = int(input("Enter Centimeter amount: "))
                    kmtoft = kilometer*3281
                    print("Answer is ", kmtoft, "ft")
                elif choice.lower()== 'b':
                    break                    
                else:
                    print("\nInvalid input, try again")
                
            elif choice.lower() == "mi":
                print("\nInto what unit?")
                print("===============")
                print("Choose one")
                print("[M]Meter")
                print("[Cm]Centimeter")
                print("[Km]Kilometer")
                print("[Yd]Yard")
                print("[In]Inch")
                print("[Ft]Foot")
                print("[B]ack")
                print("===============")
                choice=input("Pick one: ")
                
                if choice.lower()=="m":
                    print("Meter = Mile*1609")
                    mile = int(input("Enter Centieter amount: "))
                    mitom = mile*1609
                    print("Answer is ", mitom, "m")

                elif choice.lower()=="cm":
                    print("Centimeter = Mile*160900")
                    mile = int(input("Enter Centimeter amount: "))
                    mitocm = mile*160900
                    print("Answer is ", mitocm, "cm")

                elif choice.lower()=="km":
                    print("Kilometer = Mile*1.609")
                    mile = int(input("Enter Centimeter amount: "))
                    mitokm = mile*1.609
                    print("Answer is ", mitokm, "km")

                elif choice.lower()=="yd":
                    print("Yard = Mile*1760")
                    mile = int(input("Enter Centimeter amount: "))
                    mitoyd = mile*1760
                    print("Answer is ", mitoyd, "yd")

                elif choice.lower()=="in":
                    print("Inch = Mile*63360")                    
                    mile = int(input("Enter Centimeter amount: "))
                    mitoin = mile*63360
                    print("Answer is ", mitoin, "in")

                elif choice.lower()=="ft":
                    print("Foot = Mile*5280")
                    mile = int(input("Enter Centimeter amount: "))
                    mitoft = mile*5280
                    print("Answer is ", mitoft, "ft")
                elif choice.lower()== 'b':
                    break
                else:
                    print("\nInvalid input, try again")
                
            elif choice.lower() == "yd":
                print("\nInto what unit?")
                print("===============")
                print("Choose one")
                print("[M]Meter")
                print("[Cm]Centimeter")
                print("[Km]Kilometer")
                print("[Mi]Mile")
                print("[In]Inch")
                print("[Ft]Foot")
                print("[B]ack")
                print("===============")
                choice=input("Pick one: ")
                
    #EDIT THIS PART STILL NOT DONE

                if choice.lower()=="m":
                    print("Meter = Yard/1.094")
                    yard = int(input("Enter Centieter amount: "))
                    ydtom = yard/1.094
                    print("Answer is ", ydtom, "m")

                elif choice.lower()=="cm":
                    print("Centimeter = Yard*91.44")
                    yard = int(input("Enter Centimeter amount: "))
                    ydtocm = yard*91.44
                    print("Answer is ", ydtocm, "cm")

                elif choice.lower()=="km":
                    print("Kilometer = Yard/1094")
                    yard = int(input("Enter Centimeter amount: "))
                    ydtokm = yard/1094
                    print("Answer is ", ydtokm, "km")

                elif choice.lower()=="mi":
                    print("Mile = Yard/1760")
                    yard = int(input("Enter Centimeter amount: "))
                    ydtomi = yard/1760
                    print("Answer is ", ydtomi, "mi")

                elif choice.lower()=="in":
                    print("Inch = Yard*36")
                    yard = int(input("Enter Centimeter amount: "))
                    ydtoin = yard*36
                    print("Answer is ", ydtoin, "in")

                elif choice.lower()=="ft":
                    print("Foot = Yard*3")
                    yard = int(input("Enter Centimeter amount: "))
                    ydtoft = yard*3
                    print("Answer is ", ydtoft, "ft")
                elif choice.lower()== 'b':
                    break
                else:
                    print("\nInvalid input, try again")
                
            elif choice.lower() == "in":
                print("\nInto what unit?")
                print("===============")
                print("Choose one")
                print("[M]Meter")
                print("[Cm]Centimeter")
                print("[Km]Kilometer")
                print("[Mi]Mile")
                print("[Yd]Yard")
                print("[Ft]Foot")
                print("[B]ack")
                print("===============")
                choice=input("Pick one: ")

                if choice.lower()=="m":
                    print("Meter = inch/39.37")
                    inch = int(input("Enter Centieter amount: "))
                    intom = inch/39.37
                    print("Answer is ", intom, "m")

                elif choice.lower()=="cm":
                    print("Centimeter = inch*2.54")
                    inch = int(input("Enter Centimeter amount: "))
                    intocm = inch*2.54
                    print("Answer is ", intocm, "cm")

                elif choice.lower()=="km":
                    print("Kilometer = inch/39370")
                    inch = int(input("Enter Centimeter amount: "))
                    intokm = inch/39370
                    print("Answer is ", intokm, "km")

                elif choice.lower()=="mi":
                    print("Mile = inch/63360")
                    inch = int(input("Enter Centimeter amount: "))
                    intomi = inch/63360
                    print("Answer is ", intomi, "mi")

                elif choice.lower()=="yd":
                    print("Yard = inch/36")
                    inch = int(input("Enter Centimeter amount: "))
                    intoyd = inch/36
                    print("Answer is ", intoyd, "yd")

                elif choice.lower()=="ft":
                    print("Foot = inch/12")
                    inch = int(input("Enter Centimeter amount: "))
                    intoft = inch/12
                    print("Answer is ", intoft, "ft")
                elif choice.lower()== 'b':
                    break
                else:
                    print("\nInvalid input, try again")

            elif choice.lower() == "ft":
                print("\nInto what unit?")
                print("===============")
                print("Choose one")
                print("[M]Meter")
                print("[Cm]Centimeter")
                print("[Km]Kilometer")
                print("[Mi]Mile")
                print("[Yd]Yard")
                print("[In]Inch")
                print("[B]ack")
                print("===============")
                choice=input("Pick one: ")

                if choice.lower()=="m":
                    print("Meter = foot/3.281")
                    foot = int(input("Enter Centieter amount: "))
                    fttom = foot/3.281
                    print("Answer is ", fttom, "m")

                elif choice.lower()=="cm":
                    print("Centimeter = foot*30.48")
                    foot = int(input("Enter Centimeter amount: "))
                    fttocm = foot*30.48
                    print("Answer is ", fttocm, "cm")

                elif choice.lower()=="km":
                    print("Kilometer = foot/3281")
                    foot = int(input("Enter Centimeter amount: "))
                    fttokm = foot/3281
                    print("Answer is ", fttokm, "km")

                elif choice.lower()=="mi":
                    print("Mile = foot/5280")
                    foot = int(input("Enter Centimeter amount: "))
                    fttomi = foot/5280
                    print("Answer is ", fttomi, "mi")

                elif choice.lower()=="yd":
                    print("Yard = foot/3")
                    foot = int(input("Enter Centimeter amount: "))
                    fttoyd = foot/3
                    print("Answer is ", fttoyd, "yd")

                elif choice.lower()=="in":
                    print("Inch = foot*12")
                    foot = int(input("Enter Centimeter amount: "))
                    fttoin = foot*12
                    print("Answer is ", fttoin, "in")
                elif choice.lower()== 'b':
                    break
                else:
                    print("\nInvalid input, try again")
            elif choice.lower()== 'b':
                break
            else:
                print("\nInvalid input, try again")
    elif main_choice == 'X':
        print("Thank you for using this program.")
        break
    else:
        print("Invalid Choice!")
