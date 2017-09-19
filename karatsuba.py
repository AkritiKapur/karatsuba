import sys
import math
import baseconvert


def convert_base(number, input_base, output_base):
    return baseconvert.base(number, input_base, output_base, string=True)


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

    power = int(power/2)

    # Numbers are split in the form,
    # `num1_1 * 10^power + num1_2` and
    # `num2_1 * 10^power + num2_2`

    num1_1 = int((num1) / (math.pow(10, power)))
    num2_1 = int((num2) / (math.pow(10, power)))
    num1_2 = int((num1) % (math.pow(10, power)))
    num2_2 = int((num2) % (math.pow(10, power)))

    # calculates the product of
    # the two split terms of the original numbers and
    # the product of hte sum of the first terms and second terms of the numbers.
    num1_12 = karatsuba(num1_1, num2_1)
    num2_12 = karatsuba(num2_2, num1_2)
    num12 = karatsuba(num1_1 + num1_2, num2_1 + num2_2)

    return num1_12 * pow(10, power * 2) + num2_12 + (num12 - num1_12 - num2_12) * pow(10, power)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("please enter the required arguments: num1, num2, base (number)")
        sys.exit()

    else:
        num1 = int(convert_base(str(sys.argv[1]), int(sys.argv[3]), 10))
        num2 = int(convert_base(str(sys.argv[2]), int(sys.argv[3]), 10))
        product = karatsuba(num1, num2)
        print(int(convert_base(str(product), 10, int(sys.argv[3]))))
