# Category 1: Length 📏
# From	To
# Kilometres(km)	Metres(m)
# Metres(m)	Kilometres(km)
# Metres(m)	Centimetres(cm)
# Centimetres(cm)	Metres(m)
# Millimetres(mm)	Centimetres(cm)
# Miles(mi)	Kilometres(km)
# Feet(ft)	Metres(m)
# Inches( in )	Centimetres (cm)

# Category 2: Weight / Mass ⚖️
# From	To
# Kilograms(kg)	Grams(g)
# Grams(g)	Kilograms(kg)
# Milligrams(mg)	Grams(g)
# Grams(g)	Milligrams(mg)
# Pounds(lb)	Kilograms(kg)
# Ounces(oz)	Grams(g)
# Tonnes(t)	Kilograms(kg)

# Category 3: Temperature 🌡️
# From	To
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
    print("")


def mass():
    pass


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
