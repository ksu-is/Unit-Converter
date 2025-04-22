def convert_length():
    print("\nLength Conversion Options:")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Miles")
    print("3. Inches to Centimeters")
    print("4. Feet to Meters")
    print("5. Miles to Meters")
    
    choice = input("Choose an option (1-5): ")
    value = float(input("Enter value to convert: "))

    if choice == '1':
        print(f"{value} meters = {value / 1000} kilometers")
    elif choice == '2':
        print(f"{value} kilometers = {value * 0.621371} miles")
    elif choice == '3':
        print(f"{value} inches = {value * 2.54} centimeters")
    elif choice == '4':
        print(f"{value} feet = {value * 0.3048} meters")
    elif choice == '5':
        print(f"{value} miles = {value * 1609.34} meters")
    else:
        print("Invalid choice.")

def convert_temperature():
    print("\nTemperature Conversion Options:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = input("Choose an option (1-4): ")
    value = float(input("Enter value to convert: "))

    if choice == '1':
        print(f"{value}°C = {value * 9/5 + 32}°F")
    elif choice == '2':
        print(f"{value}°F = {(value - 32) * 5/9}°C")
    elif choice == '3':
        print(f"{value}°C = {value + 273.15} K")
    elif choice == '4':
        print(f"{value} K = {value - 273.15}°C")
    else:
        print("Invalid choice.")

def convert_temperature():
    print("\nTemperature Conversion Options:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = input("Choose an option (1-4): ")
    value = float(input("Enter value to convert: "))

    if choice == '1':
        print(f"{value}°C = {value * 9/5 + 32}°F")
    elif choice == '2':
        print(f"{value}°F = {(value - 32) * 5/9}°C")
    elif choice == '3':
        print(f"{value}°C = {value + 273.15} K")
    elif choice == '4':
        print(f"{value} K = {value - 273.15}°C")
    else:
        print("Invalid choice.")

def convert_weight():
    print("\nWeight Conversion Options:")
    print("1. Grams to Kilograms")
    print("2. Kilograms to Pounds")
    print("3. Pounds to Kilograms")
    print("4. Ounces to Grams")

    choice = input("Choose an option (1-4): ")
    value = float(input("Enter value to convert: "))

    if choice == '1':
        print(f"{value} grams = {value / 1000} kilograms")
    elif choice == '2':
        print(f"{value} kilograms = {value * 2.20462} pounds")
    elif choice == '3':
        print(f"{value} pounds = {value / 2.20462} kilograms")
    elif choice == '4':
        print(f"{value} ounces = {value * 28.3495} grams")
    else:
        print("Invalid choice.")
