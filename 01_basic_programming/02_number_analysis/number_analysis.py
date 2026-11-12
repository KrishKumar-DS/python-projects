def user_input():

    while True:
        try:
            num = (input("Enter the number: "))

            if "." in num:
                return float(num)

            return int(num)

        except ValueError:
            print("Invalid Input! Enter numerical value")
            continue


def check_type(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "It's Zero"


def check_parity(num):

    if "." in str(num):
        return "Float can't have parity"

    if int(num) % 2 == 0:
        return "Even"
    else:
        return "Odd"


def check_square(num):

    return num ** 2


def check_cube(num):

    return num ** 3


def check_factorial(num):
    if num < 0:
        return "Negative number can't have factorial"
    elif not num.is_integer():
        return "Factorial requires an integer"

    result = 1
    n = int(num)

    while n >= 1:
        result = result * n
        n = n - 1

    return result


def check_prime():
    pass


def count_digit(num):

    count = 0
    for i in str(num):
        if "." not in i:
            count += 1

    return count


def digit_sum(num):

    total = 0
    for i in str(num):

        if i.isdigit():
            total += int(i)

    return total


def display():
    n = user_input()

    number_type = check_type(n)
    square = check_square(n)
    cube = check_cube(n)
    parity = check_parity(n)
    factorial = check_factorial(n)
    count = count_digit(n)
    digi_sum = digit_sum(n)

    print(f"Type: {number_type}")
    print(f"Parity: {parity}")
    print(f"Square: {square}")
    print(f"Cube: {cube}")
    print(f"Factorial: {factorial}")
    print(f"Digit Count: {count}")
    print(f"Digit Sum: {digi_sum}")


def main():

    print("="*30)
    print("       NUMBER ANALYZER")
    print("="*30)

    while True:
        choice = input("Want to use Number Analyzer: ").strip().lower()

        if choice in ['y', 'yes']:
            display()

            print("="*30)

        elif choice in ['n', 'no']:
            print("Exiting......")
            break
        else:
            print("Invalid Input! Enter y/n...")
            continue


if __name__ == "__main__":
    main()
