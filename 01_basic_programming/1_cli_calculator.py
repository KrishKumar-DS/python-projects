def user_input():

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2

        except ValueError:
            print("Invalid Input! Enter only numbers")
            continue


def addition():
    num1, num2 = user_input()
    return num1 + num2


def subtraction():
    num1, num2 = user_input()
    return num1 - num2


def multiplication():
    num1, num2 = user_input()
    return num1 * num2


def division():
    while True:

        num1, num2 = user_input()
        if num2 == 0:
            print("You can't divide by zero.")
            continue

        return num1 / num2


def power():
    num1, num2 = user_input()
    return num1 ** num2


def operation():

    print("------OPERATIONS------")
    print("1. Addition\n"
          "2. Subtraction\n"
          "3. Division\n"
          "4. Multiplication\n"
          "5. Power (Exponentiation)")

    while True:

        choice = input("Which operation you want to perform: ").strip()

        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid Input!")
            continue

        elif choice == "1":
            return addition()

        elif choice == "2":
            return subtraction()

        elif choice == "3":
            return division()

        elif choice == "4":
            return multiplication()

        elif choice == "5":
            return power()


def main():

    while True:

        ask = input("Do you want to use Calculator (y/n): ").strip().lower()
        if ask == "y":
            result = operation()
            print(result)

        elif ask == "n":
            print("Thank you....")
            break

        else:
            print("Invalid input! Enter y or n.")
            continue


if __name__ == "__main__":
    main()
