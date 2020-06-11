import platform as plat


def max_bits():
    max_bits = plat.architecture()[0]
    if max_bits == "64bit":
        return 64
    if max_bits == "32bit":
        return 32

    raise TypeError("Architecture besides 64 and 32 are not supported")


def diff_bits_count(bin_num_one, bin_num_two):
    # write a function to count the number of bits that are different between two numbers
    to_shift = max_bits()
    count = 0

    for shift_count in range(0, to_shift):
        bin_num_one_shift_and = (bin_num_one >> shift_count) & 1
        bin_num_two_shift_and = (bin_num_two >> shift_count) & 1

        if bin_num_one_shift_and != bin_num_two_shift_and:
            count += 1

    return count
