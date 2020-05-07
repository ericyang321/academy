MORSES = [
    ".-",
    "-...",
    "-.-.",
    "-..",
    ".",
    "..-.",
    "--.",
    "....",
    "..",
    ".---",
    "-.-",
    ".-..",
    "--",
    "-.",
    "---",
    ".--.",
    "--.-",
    ".-.",
    "...",
    "-",
    "..-",
    "...-",
    ".--",
    "-..-",
    "-.--",
    "--..",
]


def unique_morse_code(words):
    seen = set()
    count = 0
    for word in words:
        morse_code = convert_to_morse_code(word)
        if morse_code not in seen:
            seen.add(morse_code)
            count += 1

    return count


def convert_to_morse_code(word):
    morse = ""
    for char in word:
        morse += char_to_morses(char)

    return morse


def char_to_morses(char):
    return MORSES[ord(char) - 97]
