def user_input():

    while True:
        try:
            num = float(input("Enter the number: "))
            return num

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

    if num % 2 == 0:
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
    elif num == 0:
        return 1

    if num.is_integer():
        result = 1
        n = num
        while n >= 1:
            result = result * n
            n = n - 1

    return result


def check_prime():
    pass


def count_digit(num):

    count = 0
    for i in str(num):
        count += 1

    return count


def digit_sum(num):

    total = 0
    for i in str(num):

        if i.isdigit():
            total += int(i)

    return total


def main():
    n = user_input()

    typ = check_type(n)
    typ1 = check_square(n)
    typ2 = check_parity(n)
    typ3 = check_cube(n)
    typ = check_factorial(n)
    typ4 = count_digit(n)
    typ5 = digit_sum(n)

    print(typ)
    print(typ1)
    print(typ2)
    print(typ3)
    print(typ4)
    print(typ5)


if __name__ == "__main__":
    main()
