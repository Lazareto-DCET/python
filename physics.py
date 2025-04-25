def calculate_resistance(voltage, current):
    if current == 0:
        return "Error! Current cannot be zero."
    return voltage / current

def calculate_voltage(current, resistance):
    return current*resistance

def calculate_current(voltage, resistance):
    if resistance == 0:
        return "Error! Resistance cannot be zero."
    return voltage / resistance

def calculate_charge(capacitance, voltage):
    return capacitance*voltage

def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

def gravitational_potential_energy(mass, gravity, height):
    return mass * gravity * height

def force(mass, acceleration):
    return mass * acceleration

def weight(mass, gravity):
    return mass*gravity

def main():
    while True:
        print("\n<========== Welcome to the Engineering Calculator! ==========>")
        print("This is a simple calculator made by Samiano. It has 3  type of calculator below. I hope you like this app.")
        print("Enjoy !!!")
        print("1. Weight Conversion")
        print("2. Physics Calculator")
        print("3. Electronics Calculator")
        print("4. Exit")
        choice = input("Please select an option: ")

        if choice == '4':
            print("Thank you for using the program :)")
            break

        if choice == '1':
            weight_conversion()
        elif choice == '2':
            physics_calculator()
        elif choice == '3':
            electronics_calculator()
        else:
            print("Invalid input! Please select a valid option.")
def weight_conversion():
    while True:
        print("\n-------- Weight Conversion --------")
        print("1. Kilogram to gram")
        print("2. Gram to milligram")
        print("3. Kilogram to pound")
        print("4. Pound to Ounce")
        print("5. Go back to main menu")
        choice = input("Please select an operation: ")

        if choice == '5':
            break

        try:
            if choice == '1':
                  kg = float(input("Enter Kilograms: "))
                  print(f"{kg} Kilograms = {kg * 1000} g")
            elif choice == '2':
                gram = float(input("Enter Grams: "))
                print(f"{gram} Grams = {gram*1000} mg")
            elif choice == '3':
                kg = float(input("Enter Kilogram: "))
                print(f"{kg} Kilograms = {kg*2.2} lbs")                
            elif choice == '4':
                lbs = float(input("Enter Pounds: "))
                print(f"{lbs} Pounds = {lbs*16} oz")   
            else:
                print("Invalid input! Please select a valid operation.")
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

def physics_calculator():
    while True:
        print("\n<========== Physics Calculator ==========>")
        print("1. Kinetic Energy")
        print("2. Gravitational Potential Energy")
        print("3. Force")
        print("4. Weight")
        print("5. Go back to main menu")
        choice = input("Please select an operation: ")

        if choice == '5':
            break

        try:
            if choice == '1':
                mass = float(input("Enter mass (kg): "))
                velocity = float(input("Enter velocity (m/s): "))
                print("KE = 1/2 * mass * velocity^2")
                print(f"Kinetic Energy: {kinetic_energy(mass, velocity)} J")
            elif choice == '2':
                mass = float(input("Enter mass (kg): "))
                gravity = 9.81
                height = float(input("Enter height (m): "))
                print("U = mass*gravity*height")
                print(f"Gravitational Potential Energy: {gravitational_potential_energy(mass, gravity, height)} J")
            elif choice == '3':
                mass = float(input("Enter mass (kg): "))
                acceleration = float(input("Enter acceleration (m/s^2): "))
                print("F = mass*acceleration")
                print(f"Force: {force(mass, acceleration)} N")
            elif choice == '4':
                mass = float(input("Enter mass (kg): "))
                gravity = 9.81
                print("W = m*g")
                print(f"Weight: {weight(mass, gravity)}N")    
            else:
                print("Invalid input! Please select a valid operation.")
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

def electronics_calculator():
    while True:
        print("\n:::::-------- Electronics Calculator --------::::")
        print("1. Calculate Resistance")
        print("2. Calculate Voltage")
        print("3. Calculate Current")
        print("4. Calculate Charge")
        print("5. Go back to main menu")
        choice = input("Please select an operation: ")

        if choice == '5':
            break

        try:
            if choice == '1':
                voltage = float(input("Enter voltage (V): "))
                current = float(input("Enter current (A): "))
                print("R = V/I")
                print(f"Resistance: {calculate_resistance(voltage, current)} Ohms")
            elif choice == '2':
                current = float(input("Enter current (I): "))
                resistance = float(input("Enter resistance (R): "))
                print("V = I*R")
                print(f"Voltage: {calculate_voltage(current, resistance)} Volts")
            elif choice == '3':
                voltage = float(input("Enter voltage (V): "))
                resistance = float(input("Enter resistance (Ohms): "))
                print("I = V/R")
                print(f"Current: {calculate_current(voltage, resistance)} Amps")
            elif choice =='4':
                capacitance = float (input("Enter capacitance (C): "))
                voltage = float(input("Enter voltage (V): "))
                print("Q = C*V")
                print(f"Charge: {calculate_charge(capacitance, voltage)} Q")
            else:
                print("Invalid input! Please select a valid operation.")
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
if __name__ == "__main__":
    main()           
