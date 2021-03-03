# https://leetcode.com/problems/alien-dictionary/

from collections import defaultdict, deque


class PrefixError(ValueError):
    pass


class CycleError(ValueError):
    pass


def build_adjacency_list(words):
    graph = {}

    for idx in range(1, len(words)):
        word = words[idx]
        prev_word = words[idx - 1]

        # search until we find two characters that aren't the same
        for char_idx in range(min(len(word), len(prev_word))):
            char = word[char_idx]
            prev_char = prev_word[char_idx]

            if char != prev_char:
                if prev_char not in graph:
                    graph[prev_char] = set()

                graph[prev_char].add(char)
                break
        # if a loop has finished and no different characters are found, ensure
        # the later word is a longer one. otherwise the string is invalid
        else:
            if len(word) < len(prev_word):
                raise PrefixError

    return graph


def build_indegrees(adjacency_list, words):
    indegrees = {}

    # add every alphabet as 0 from words
    for word in words:
        for char in word:
            if char not in indegrees:
                indegrees[char] = 0
    # count incoming connections of every node
    for source_node, dest_node_set in adjacency_list.items():
        if source_node not in indegrees:
            indegrees[source_node] = 0

        for dest_node in dest_node_set:
            if dest_node not in indegrees:
                indegrees[dest_node] = 0

            indegrees[dest_node] += 1

    return indegrees


def kahns_algorithm(adjacency_list, words):
    indegrees = build_indegrees(adjacency_list, words)

    ordered_elements = []
    q = deque([])
    for node, indegree in indegrees.items():
        if indegree == 0:
            q.appendleft(node)

    while q:
        node = q.pop()
        ordered_elements.append(node)

        # don't traverse any neighbors if there aren't any
        if node not in adjacency_list:
            continue

        # traverse neighbors and deduct their indegrees as an act of traversing
        for neighbor in adjacency_list[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                q.appendleft(neighbor)

    # loop detected
    if len(ordered_elements) != len(indegrees):
        raise CycleError

    return ordered_elements


def alien_alphabet_order(words):
    """
    There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.
    You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

    Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

    A string is lexicographically ordered as:
    - _the first different letter_ in prev_string is smaller than next_string if prev_string idx is smaller than next_string idx.
    - if prev_string is a prefix (all the chars in prev_strings are also in next_string, in the exact order) of next_string, then prev_string is smaller IF prev_string len is shorter
    than next_string.
    """
    try:
        word_graph = build_adjacency_list(words)
    except PrefixError:
        return ""

    try:
        ordered_chars = kahns_algorithm(word_graph, words)
    except CycleError:
        return ""

    return "".join(ordered_chars)
