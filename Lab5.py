def is_valid_part(part):
    if not part.isdigit():
        return False

    num = int(part)

    if num < 0 or num > 255:
        return False

    if part[0] == '0' and len(part) > 1:
        return False

    return True


def is_valid_ip(ip):
    parts = ip.split('.')

    if len(parts) != 4:
        return False

    for part in parts:
        if not is_valid_part(part):
            return False

    return True


user_input = input("Enter an IP address: ")

if is_valid_ip(user_input):
    print(f"'{user_input}' is a valid IP address.")
else:
    print(f"'{user_input}' is NOT a valid IP address.")







