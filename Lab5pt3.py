def binary_to_decimal(b):

    if b == "":
        return 0

    return int(b[0]) * (2 ** (len(b) - 1)) + binary_to_decimal(b[1:])


binary_input = input("Enter a binary number: ")

decimal_output = binary_to_decimal(binary_input)
print(f"The decimal representation of {binary_input} is: {decimal_output}")
