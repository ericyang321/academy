def pattern_match_str(string, substring):
    string_len = len(string)
    substring_len = len(substring)
    if substring_len == 0:
        return 0

    # create last idx of alphabet look up table,
    # later repeat alphabet occurances overwrite earlier alphabet occurances
    last = {}
    for idx, char in enumerate(substring):
        last[char] = idx

    print(last)

    # idx pointer for keeping track of current substring and string char comparison
    string_idx = substring_len - 1
    substring_idx = substring_len - 1
    print(f"starting at string char {string[string_idx]}, {string_idx}")
    print(f"starting at substring char {substring[substring_idx]}, {substring_idx}")
    while string_idx < string_len:
        # found two characters that match
        if string[string_idx] == substring[substring_idx]:
            # if substring_idx exhausted and all of the pattern is matched, we're done
            print(f"char match: string_idx={string_idx} == substring_idx={substring_idx}")
            if substring_idx == 0:
                print(f"found. {string_idx}")
                return string_idx
            # if the entire pattern isn't matched, match more
            else:
                string_idx -= 1
                substring_idx -= 1
        # the character is mismatched. find where the next matched location is
        else:
            last_match_idx = last.get(string[string_idx], -1)
            print(f"mismatch. the next char for {string[string_idx]} is at {last_match_idx}")
            # the mismatched character doesn't exist in the substring. skip by substring_len
            if last_match_idx == -1:
                print(f"mismatched char doesn't exist in substring | advance string_idx by {substring_len}")
                string_idx += substring_len
            # the mismatched character exists in the substring
            else:
                print(f"mismatched char exists in substring | advance string_idx by ({substring_len} - {substring_idx}) = {substring_len - substring_idx}")
                string_idx += (substring_len - substring_idx)

            substring_idx = substring_len - 1

    return -1
