# brian kernighan's way to count bits
def count_bits(bin_num):
    # write a function to count the number of set bits (1s) in a number
    count = 0
    while bin_num > 0:
        count += (bin_num & 1)
        bin_num = bin_num >> 1

    return count
