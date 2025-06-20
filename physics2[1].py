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
