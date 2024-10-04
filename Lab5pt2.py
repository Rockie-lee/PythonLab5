def decimal_to_binary(n):

    if n == 0:
        return "0"

    if n == 1:
        return "1"

    return decimal_to_binary(n // 2) + str(n % 2)

decimal_input = int(input("Enter a decimal number: "))

binary_output = decimal_to_binary(decimal_input)
print(f"The binary representation of {decimal_input} is: {binary_output}")
