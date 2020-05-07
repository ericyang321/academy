def self_dividing_numbers(left, right):
    """
    O(n), where n = number of integers between left and right
    """
    result = []
    for i in range(left, right + 1):
        if can_divide_its_subnumbers(i) is True:
            result.append(i)

    return result


def can_divide_its_subnumbers(number):
    parts = subnumbers_via_string(number)
    for num in parts:
        if num == 0:
            return False

        if number % num != 0:
            return False

    return True


def subnumbers_via_string(number):
    """
    convert to string and iterating each char
    and converting char to int
    """
    parts_int = []
    stringified_ints = str(number)
    for string in stringified_ints:
        parts_int.append(int(string))

    return parts_int


def subnumbers_via_division(number):
    """
    continuously divide this by 10 until it passes 0
    """
    parts_int = []
    n = number
    while n > 0:
        n = n / 10
        parts_int.append(n)
