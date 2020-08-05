# On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.
# A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

# The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

# Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

# Examples:

# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.
# Input: board = [[1,2,3],[5,4,0]]
# Output: -1
# Explanation: No number of moves will make the board solved.
# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.
# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]
# Input: board = [[3,2,4],[1,5,0]]
# Output: 14
# Note:

# board will be a 2 x 3 array as described above.
# board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].

from collections import deque
from copy import deepcopy
import heapq

"""
constraints

accepts 2x3 array with ints 1 - 5 and a 0
if the board can become [[1, 2, 3], [4, 5, 0]], return the least number of moves taken to get there
else return -1

will i need to check if all the pieces are unique? (no)
pieces can only "slide" into place and cannot jump between squares right? (yes)
will the board always be 2x3? do I need to design for the future where the board can be any size? (not for now. maybe as an optimization later)

ideas

this is essentially a shortest path problem, where the edges are moves and the vertices are board states
the cost of each move is the same: 1. so how do you find shortest distance when all moves are 1?

you do it with _breadth first search_ as a brute force approach.
and then we can optimize with A* instead

complexities
brute force BFS requires us to create factorial combinations of row * column:
n = # of rows
m = # or columns

O((n * m)!)

A*
"""

DESIRED_BOARD = [[1, 2, 3], [4, 5, 0]]


def is_solved(board):
    return board == [[1, 2, 3], [4, 5, 0]]


def find_coord(board, wanted_num):
    # searches for and returns (row_index, column_index) position if a wanted number
    # in a given board
    for row_idx, row in enumerate(board):
        for col_idx, num in enumerate(row):
            if wanted_num == num or wanted_num == str(num):
                return (row_idx, col_idx)

    return (None, None)


def find_zero(board):
    for row_idx, row in enumerate(board):
        for tile_idx, tile in enumerate(row):
            if tile == 0 or tile == "0":
                return (row_idx, tile_idx)

    return (None, None)


def swap(board, coord, other_coord):
    x_coord, y_coord = coord
    other_x_coord, other_y_coord = other_coord

    temp = board[x_coord][y_coord]
    board[x_coord][y_coord] = board[other_x_coord][other_y_coord]
    board[other_x_coord][other_y_coord] = temp


def in_bounds(board, row_idx, col_idx):
    return 0 <= row_idx < len(board) and 0 <= col_idx < len(board[0])


def get_swappables(board, zero_coord):
    x, y = zero_coord
    coords = [
        (x - 1, y),  # top
        (x + 1, y),  # bottom
        (x, y - 1),  # left
        (x, y + 1),  # right
    ]
    return [coord for coord in coords if in_bounds(board, coord[0], coord[1])]


def bfs_approach(board):
    visited = set()
    q = deque([(0, board)])
    while q:
        depth, b = q.pop()

        if is_solved(b):
            return depth

        visited.add(str(b))

        zero_coord = find_zero(b)
        next_steps = get_swappables(b, zero_coord)
        for next_step in next_steps:
            duped_board = deepcopy(b)
            swap(duped_board, zero_coord, next_step)

            if str(duped_board) not in visited:
                q.appendleft((depth + 1, duped_board))

    return -1

# ====================== A* approach methods =========================

def manhattan_distance(current_coordinates, desired_coordinates):
    # mathematical formula for calculating manhattan / taxi cab distance
    # https://math.stackexchange.com/questions/139600/how-do-i-calculate-euclidean-and-manhattan-distance-by-hand
    x1, y1 = current_coordinates
    x2, y2 = desired_coordinates

    return abs(x1 - x2) + abs(y1 - y2)

def aggregate_manhattan_distances(board, desired_board):
    # calculate the manhattan distance of each unique number from their
    # desired positions
    # save result to a hash structured like {1: 0, 2: 3, 4: 1}...
    # and then add all the values up, return it as a final resultant distance
    distances_tally = {}
    for row_idx, row in enumerate(board):
        for col_idx, num in enumerate(row):
            current_coordinates = (row_idx, col_idx)
            desired_coordinates = find_coord(desired_board, num)
            distances_tally[num] = manhattan_distance(current_coordinates, desired_coordinates)

    total = 0
    for distances in distances_tally.values():
        total += distances

    return total

def a_star_approach(board):
    costs = {str(board): 0}
    heap = [(0, 0, board)]

    boards_checked = 0

    while heap:
        current_cost, depth, node = heapq.heappop(heap)
        # problem is solved. return steps it took to solve it
        if is_solved(node):
            return depth

        # if current path is not as cheap as what's already recorded, skip
        if costs[str(node)] < current_cost:
            continue

        # find where zero is in current board move
        zero_coord = find_zero(node)
        swappable_neighbor_coordinates = get_swappables(node, zero_coord)

        for swappable_coordinate in swappable_neighbor_coordinates:
            # duplicate board for modification
            duped_board = deepcopy(node)
            # swap zero with a neighbor
            swap(duped_board, zero_coord, swappable_coordinate)
            # calculate heuristic + depth for heap sorting
            heuristic = aggregate_manhattan_distances(duped_board, DESIRED_BOARD)
            cost = depth + 1 + heuristic

            if str(duped_board) not in costs:
                costs[str(duped_board)] = float("inf")

            if cost < costs[str(duped_board)]:
                costs[str(duped_board)] = cost

                # create and push heap node into heap
                heapq.heappush(heap, (cost, depth + 1, duped_board))


    return -1
