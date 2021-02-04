def longest_substring_k_distinct(string, k):
    # find the longest substring where only k distinct characters are allowed
    # for example: AAAHHIBC returns AAAHHI
    chars = {}

    start_idx = 0
    longest_count = 0

    buf = []
    longest_str = ""
    for end_idx in range(len(string)):
        right_char = string[end_idx]
        chars.setdefault(right_char, 0)
        chars[right_char] += 1
        buf.append(right_char)

        while len(chars) > k:
            left_char = string[start_idx]
            chars[left_char] -= 1
            buf.pop(0)
            if chars[left_char] == 0:
                del chars[left_char]

            start_idx += 1

        diff = end_idx - start_idx + 1
        if diff > longest_count:
            longest_count = diff
            longest_str = "".join(buf)

    return longest_str
