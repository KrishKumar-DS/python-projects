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

    operations = {
        "1": addition,
        "2": subtraction,
        "3": division,
        "4": multiplication,
        "5": power
    }

    loop = True
    while loop:

        choice = input("Which operation you want to perform: ").strip()

        if choice == "":
            print("Operation can't be empty!")
            continue

        elif choice not in operations:
            print("Please choose operation from the above choices.")
            continue

        selected_operation = operations[choice]

        op = selected_operation()

        print(op)

        while True:
            cont = input(
                "Do you want to perform another calculation? (y/n): ").strip().lower()

            if cont == 'y':
                print("Continuing....")
                break
            elif cont == 'n':
                print("Exiting......")
                loop = False
                break
            else:
                print("Invalid Input!")
                continue


def main():

    while True:

        ask = input("Do you want to use Calculator (y/n): ").strip().lower()
        if ask == "y":
            operation()

        elif ask == "n":
            print("Thank you....")
            break

        else:
            print("Invalid input! Enter y or n.")
            continue


if __name__ == "__main__":
    main()
