# accepts an array of integers.
# can contain multiple utf-8 characters in a single array in sequence. will return true as long as multiple characters are all utf-8 format

# the rules of utf-8 are as follows:
# 1. a single valid utf-8 char is 1 - 4 bytes long
# 2. for a 1 byte char, the char starts with a 0, followed by it's unicode
# 3. for N bytes long char, the first X bits are all 1s, followed by a 0 on X + 1 bit. Then, N - 1 bytes (max up to 3 trailing N - 1 bytes) that follow all start with `10`

# each integer in the array can be larger than 8 bits (larger than 255). we only read from the 8 least significant bits of each integer.
def utf8_validator(data):
    n_bytes = 0
    for num in data:
        # if this is a leading byte
        if n_bytes == 0:
            n_bytes = num_of_bytes(num)
            # this is a one byte character
            if n_bytes == 0:
                continue

            # invalid scenario: leading byte indicates theres more than 4 bytes in the character
            # invalid scenario: incorrect formatting. `10` is not accepted. there needs to at least be `110` to indicate at one trailing byte
            if n_bytes > 4 or n_bytes == 1:
                return False
        # if this is a trailing byte
        else:
            if not is_trailing_byte(num):
                return False

        n_bytes -= 1

    # all trailing bytes must be terminated, and no leading bytes are left hanging
    return n_bytes == 0

def num_of_bytes(head_byte):
    n_bytes = 0
    # create a mask starting from 8th most significant digit
    mask = 1 << 7
    while mask & head_byte != 0:
        n_bytes += 1
        mask = mask >> 1

    return n_bytes

def is_trailing_byte(byte):
    one_mask = 1 << 7
    zero_mask = 1 << 6

    return (byte & one_mask) and not (byte & zero_mask)

# number of bytes in current UTF-8 char
