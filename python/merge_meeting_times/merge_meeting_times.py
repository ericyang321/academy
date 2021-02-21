def merge_meeting_times(meeting_times):
    """
    Write a function merge_meeting_times() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.

    For example, given:

    [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

    your function would return:

    [(0, 1), (3, 8), (9, 12)]

    Do not assume the meetings are in order. The meeting times are coming from multiple teams.
    """

    """
    my take away from this question:

    1. the array will not be sorted
    2. input is an array of tuples, and returned results is an array of tuples, with overlapping ranges merged together.
    3. there can be no negative numbers

    sorting (based on starting times value of the tuples) sounds like a good initial brute force. because then we can iterate
    through the sorted tuples in order and glob together glob-able meeting times without having to look through an array over
    and over again for potential glob-able candidates.

    walk through examples:

    [(1, 2), (8, 9), (2, 3)] -> [(1, 2), (2, 3), (8, 9)] -> [(1, 3), (8, 9)]
    [(0, 0), (0, 0)] -> [(0, 0), (0, 0)] -> [(0, 0)]
    [(1, 2), (8, 9), (0, 10)] -> [(0, 10), (1, 2), (8, 9)] -> [(0, 10)]

    the solution feels like it makes sense. walk through it:

    1. sort array based on first digit of tuple
    2. iterate over list with two indices: predator_idx and prey_idx
        3. if [predator_idx] and [prey_idx] are NOT overlapping, predator_idx = prey_idx and prey_idx += 1
        4. if they overlap, you need to glob them.
        5. if predator start idx is smaller than prey idx (means predator's meeting time starts earlier), use predator idx's meeting time | vice versa
        6. if predator end idx is larger than prey idx (means predator's meeting time ends later), use predator's idx meeting time | vice versa
        7. prey_idx += 1

    8. return array
    """

    merged_times = sorted(meeting_times, key=lambda tup: tup[0])
    predator_idx = 0
    prey_idx = 1

    while prey_idx < len(merged_times):
        predator = merged_times[predator_idx]
        prey = merged_times[prey_idx]

        if is_overlapping(predator, prey):
            merged_time_tuple = merge_time_tuples(predator, prey)
            merged_times[predator_idx] = merged_time_tuple

            del merged_times[prey_idx]
        else:
            predator_idx = prey_idx
            prey_idx += 1

    return merged_times


def is_overlapping(predator, prey):
    return (prey[0] <= predator[1] and prey[0] >= predator[0]) or (
        prey[1] <= predator[1] and prey[1] >= predator[0]
    )


def merge_time_tuples(predator, prey):
    out = [None, None]

    out[0] = predator[0] if predator[0] <= prey[0] else prey[0]
    out[1] = predator[1] if predator[1] >= prey[1] else prey[1]

    return tuple(out)
