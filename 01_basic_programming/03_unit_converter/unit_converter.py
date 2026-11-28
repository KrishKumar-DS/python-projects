# Celsius(°C)	Fahrenheit(°F)
# Fahrenheit(°F)	Celsius(°C)
# Celsius(°C)	Kelvin(K)
# Kelvin(K)	Celsius(°C)
# Fahrenheit(°F)	Kelvin(K)
# Kelvin(K)	Fahrenheit(°F)


# Category 4: Time ⏱️
# From	To
# Seconds	Minutes
# Minutes	Hours
# Hours	Minutes
# Hours	Days
# Days	Hours
# Days	Weeks
# Weeks	Days

# Category 5: Speed 🚀
# From	To
# km/h	m/s
# m/s	km/h
# mph	km/h
# km/h	mph

# Category 6: Data Storage 💾
# From	To
# Bytes(B)	Kilobytes(KB)
# Kilobytes(KB)	Bytes(B)
# Kilobytes(KB)	Megabytes(MB)
# Megabytes(MB)	Kilobytes(KB)
# Megabytes(MB)	Gigabytes(GB)
# Gigabytes(GB)	Megabytes(MB)
# Gigabytes(GB)	Terabytes(TB)
# Terabytes(TB)	Gigabytes(GB)

def length():
    print("You select Length Unit Converter")
    print("Available conversions:-")
    print("1. Kilometres(km)  ->  Metres(m)"
          "2. Metres(m)  ->  Kilometres(km)"
          "3. Metres(m)  ->  Centimetres(cm)"
          "4. Centimetres(cm)  ->  Metres(m)"
          "5. Millimetres(mm)  ->  Centimetres(cm)"
          "6. Miles(mi)  ->  Kilometres(km)"
          "7. Feet(ft)  ->  Metres(m)"
          "8. Inches( in )  ->  Centimetres (cm)")
    selection = input("Enter the number: ")


def mass():
    print("You select Mass/Weight Unit Converter")
    print("Available conversions:-")
    print("1. Kilograms(kg)  ->  Grams(g)"
          "2. Grams(g)  ->  Kilograms(kg)"
          "3. Milligrams(mg)  ->  Grams(g)"
          "4. Grams(g)  ->  Milligrams(mg)"
          "5. Pounds(lb)  ->  Kilograms(kg)"
          "6. Ounces(oz)  ->  Grams(g)"
          "7. Tonnes(t)  ->  Kilograms(kg)")

    selection = input("Enter the number: ")


def temperature():
    pass


def time():
    pass


def speed():
    pass


def data_storage():
    pass


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

        if category == "":
            print("")
            continue
        elif category.lower() == "exit":
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
