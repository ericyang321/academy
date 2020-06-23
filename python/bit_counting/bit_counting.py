import platform as plat


def max_bits():
    max_bits = plat.architecture()[0]
    if max_bits == "64bit":
        return 64
    if max_bits == "32bit":
        return 32

    raise TypeError("Architecture besides 64 and 32 are not supported")

# using loop to iterate over all possible existing bits
def diff_bits_count(bin_num_one, bin_num_two):
    # write a function to count the number of bits that are different between two numbers
    to_shift = max_bits()
    count = 0

    # from 0 -> maximum number of bit positions
    # shift checked bit position to 2^0 digit and & 1
    # if the number is 0, & will return 0. if the number is 1, & will return 1
    # check if both numbers return the same AND comparisons to determine if
    # they're the same bits
    for shift_count in range(0, to_shift):
        bin_num_one_shift_and = (bin_num_one >> shift_count) & 1
        bin_num_two_shift_and = (bin_num_two >> shift_count) & 1

        if bin_num_one_shift_and != bin_num_two_shift_and:
            count += 1

    return count

# brian kernighan's way to count bits
def brians_way(bin_num):
    # write a function to count the number of set bits (1s) in a number
    count = 0
    while bin_num > 0:
        count += (bin_num & 1)
        bin_num = bin_num >> 1

    return count