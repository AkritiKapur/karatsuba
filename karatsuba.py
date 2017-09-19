import math


def convert_base():
    pass


def reconvert_base():
    pass


def karatsuba(num1, num2):
    """
        Function multiplies two integers recursively reducing the total multiplications
        from four to three.
    :param num1: first number to be multiplied
    :param num2: second number to be multiplied
    :return: product of num1 and num2
    """

    if num1 < 10 or num2 < 10:
        return num1 * num2

    power = max(len(str(num1)), len(str(num2)))

    power = power/2

    # Numbers are split in the form,
    # `num1_1 * 10^power + num1_2` and
    # `num2_1 * 10^power + num2_2`

    num1_1 = int(num1) / int(math.pow(10, power))
    num2_1 = int(num2) / int(math.pow(10, power))
    num1_2 = int(num1) % int(math.pow(10, power))
    num2_2 = int(num2) % int(math.pow(10, power))

    # calculates the product of
    # the two split terms of the original numbers and
    # the product of hte sum of the first terms and second terms of the numbers.
    num1_12 = karatsuba(num1_1, num2_1)
    num2_12 = karatsuba(num2_2, num1_2)
    num12 = karatsuba(num1_1 + num1_2, num2_1 + num2_2)

    return num1_12 * pow(10, power * 2) + num2_12 + (num12 - num1_12 - num2_12) * pow(10, power)


if __name__ == "__main__":
    print karatsuba(245, 789)
