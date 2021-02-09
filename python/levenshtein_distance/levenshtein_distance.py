def levenshtein(string1, string2):
    # i points to string1 terminal index
    # j points to string2 terminal index

    if min(len(string1), len(string2)) == 0:
        return max(len(string1), len(string2))

    matrix = [[0 for _ in range(len(string2) + 1)] for _ in range(len(string1) + 1)]

    for i in range(len(string1) + 1):
        for j in range(len(string2) + 1):
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            else:
                points_from_actions = [
                    matrix[i - 1][j] + 1,
                    matrix[i][j - 1] + 1,
                    matrix[i - 1][j - 1]
                ]

                if string1[i - 1] != string2[j - 1]:
                    points_from_actions[2] += 1

                print(points_from_actions)
                matrix[i][j] = min(points_from_actions)

    return matrix[-1][-1]
