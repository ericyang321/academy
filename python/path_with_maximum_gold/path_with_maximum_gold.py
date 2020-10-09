# https://leetcode.com/problems/path-with-maximum-gold/

def viable_neighbors(grid, coord):
    y, x = coord
    possible_coords = [
        (y - 1, x),
        (y, x + 1),
        (y + 1, x),
        (y, x - 1),
    ]
    viable_coords = []
    for possible_y, possible_x in possible_coords:
        if (
            0 <= possible_y < len(grid)
            and 0 <= possible_x < len(grid[0])
            and grid[possible_y][possible_x] != 0
        ):
            viable_coords.append((possible_y, possible_x))

    return viable_coords


def dfs(grid, coord, visited, gold):
    visited.add(coord)
    neighbors = viable_neighbors(grid, coord)
    new_gold = gold + grid[coord[0]][coord[1]]

    possible_golds = []

    for neighbor in neighbors:
        if neighbor not in visited:
            explored_gold = dfs(grid, neighbor, visited, new_gold)
            possible_golds.append(explored_gold)

    visited.remove(coord)
    return max(possible_golds or [new_gold])


def solve(grid):
    max_gold = 0
    visited = set()

    for y, row in enumerate(grid):
        for x, gold_amount in enumerate(row):
            if gold_amount != 0:
                gold_found = dfs(grid, (y, x), visited, 0)
                if gold_found > max_gold:
                    max_gold = gold_found

            visited.clear()

    return max_gold


grid = [
    [1, 0, 7, 0, 0, 0],
    [2, 0, 6, 0, 1, 0],
    [3, 5, 6, 7, 4, 2],
    [4, 3, 1, 0, 2, 0],
    [3, 0, 5, 0, 20, 0],
]
print(solve(grid))
