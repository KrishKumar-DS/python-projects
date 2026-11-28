def length():
    print("You select Length Unit Converter")
    print("Available conversions:-")
    print(
        "1. Kilometres(km)  ->  Metres(m)\n"
        "2. Metres(m)  ->  Kilometres(km)\n"
        "3. Metres(m)  ->  Centimetres(cm)\n"
        "4. Centimetres(cm)  ->  Metres(m)\n"
        "5. Millimetres(mm)  ->  Centimetres(cm)\n"
        "6. Miles(mi)  ->  Kilometres(km)\n"
        "7. Feet(ft)  ->  Metres(m)\n"
        "8. Inches( in )  ->  Centimetres (cm)\n"
    )

    selection = input("Enter the number: ")


def mass():

    print("You select Mass/Weight Unit Converter")
    print("Available conversions:-")
    print(
        "1. Kilograms(kg)  ->  Grams(g)\n"
        "2. Grams(g)  ->  Kilograms(kg)\n"
        "3. Milligrams(mg)  ->  Grams(g)\n"
        "4. Grams(g)  ->  Milligrams(mg)\n"
        "5. Pounds(lb)  ->  Kilograms(kg)\n"
        "6. Ounces(oz)  ->  Grams(g)\n"
        "7. Tonnes(t)  ->  Kilograms(kg)\n"
    )

    selection = input("Enter the number: ")


def temperature():

    print("You select Temperature Unit Converter")
    print("Available conversions:-")
    print(
        "1. Celsius(°C)  ->  Fahrenheit(°F)\n"
        "2. Fahrenheit(°F)  ->  Celsius(°C)\n"
        "3. Celsius(°C)  ->  Kelvin(K)\n"
        "4. Kelvin(K)  ->  Celsius(°C)\n"
        "5. Fahrenheit(°F)  ->  Kelvin(K)\n"
        "6. Kelvin(K)  ->  Fahrenheit(°F)\n"
    )

    selection = input("Enter the number: ")


def time():

    print("You select Time Unit Converter")
    print("Available conversions:-")
    print(
        "1. Seconds  ->  Minutes\n"
        "2. Minutes  ->  Hours\n"
        "3. Hours  ->  Minutes\n"
        "4. Hours  ->  Days\n"
        "5. Days  ->  Hours\n"
        "6. Days  ->  Weeks\n"
        "7. Weeks  ->  Days\n"
    )

    selection = input("Enter the number: ")


def speed():

    print("You select Speed Unit Converter")
    print("Available conversions:-")
    print(
        "1. km/h  ->  m/s\n"
        "2. m/s  ->  km/h\n"
        "3. mph  ->  km/h\n"
        "4. km/h  ->  mph\n"
    )

    selection = input("Enter the number: ")


def data_storage():

    print("You select Data Storage Unit Converter")
    print("Available conversions:-")
    print(
        "1. Bytes(B)  ->  Kilobytes(KB)\n"
        "2. Kilobytes(KB)  ->  Bytes(B)\n"
        "3. Kilobytes(KB)  ->  Megabytes(MB)\n"
        "4. Megabytes(MB)  ->  Kilobytes(KB)\n"
        "5. Megabytes(MB)  ->  Gigabytes(GB)\n"
        "6. Gigabytes(GB)  ->  Megabytes(MB)\n"
        "7. Gigabytes(GB)  ->  Terabytes(TB)\n"
        "8. Terabytes(TB)  ->  Gigabytes(GB)\n"
    )

    selection = input("Enter the number: ")


def unit_selection():
    print("Category of Unit Conversions")

    print("Category 1: Length\n"
          "Category 2: Mass/Weight\n"
          "Category 3: Temperature\n"
          "Category 4: Time\n"
          "Category 5: Speed\n"
          "Category 6: Data Storage\n")

    while True:
        category = input("Enter the Category you want to select: ").strip()

        if category.lower() == "exit":
            print("Exiting...")
            break

        elif category == "1":
            length()
        elif category == "2":
            mass()
        elif category == "3":
            temperature()
        elif category == "4":
            time()
        elif category == "5":
            speed()
        elif category == "6":
            data_storage()
        else:
            print("Invalid Input! Try Again, Enter the number of category.")
            continue


def display_result():
    pass


def main():
    pass
