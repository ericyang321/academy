def to_lowercase(str):
    lowered_string = ""
    for char in str:
        if is_upper_case(char):
            lowered_string = lowered_string + convert_to_lower_case(char)
        else:
            lowered_string = lowered_string + char

    return lowered_string


def is_lower_case(char):
    ascii_code = ord(char)
    if ascii_code >= 97 and ascii_code <= 122:
        return True

    return False


def is_upper_case(char):
    ascii_code = ord(char)
    if ascii_code >= 65 and ascii_code <= 90:
        return True

    return False


def convert_to_lower_case(char):
    return chr(ord(char) + 32)
