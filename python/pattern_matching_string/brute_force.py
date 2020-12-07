def pattern_match_str(string, substring):
    """
    return lowest index position of found substring. otherwise return -1
    for every character in string,
    """
    string_len = len(string)
    substring_len = len(substring)

    if substring_len > string_len:
        raise ValueError("Substring cannot be longer than string")

    for idx in range(string_len - substring_len + 1):
        substring_idx = 0
        # if a first character of current string == first character of substring,
        # check every consecutive character afterwards.
        while (
            substring_idx < substring_len
            and string[idx + substring_idx] == substring[substring_idx]
        ):
            substring_idx += 1
        # if we finish the exhaustive consecutive check and it's the same string, return
        if substring_idx == substring_len:
            return idx

    # couldn't find any matching strings
    return -1
