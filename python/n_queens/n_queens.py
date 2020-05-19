# n queens
class NQueensSolver(object):
    def __init__(self, board_width, board_height):
        self.max_x = board_width
        self.max_y = board_height

    def all_coordinates(self):
        s = set()
        for x in range(1, self.max_x + 1):
            for y in range(1, self.max_y + 1):
                s.add((x, y))

        return s

    def get_left_leaning_diagonals(self, x, y):
        coords = []

        diag_x = x - 1
        diag_y = y + 1
        while diag_x >= 0 and diag_y <= self.max_y:
            coords.append((diag_x, diag_y))
            diag_x -= 1
            diag_y += 1

        diag_x = x + 1
        diag_y = y - 1
        while diag_x <= self.max_x and diag_y >= 0:
            coords.append((diag_x, diag_y))
            diag_x += 1
            diag_y -= 1

        return coords

    def get_right_leaning_diagonals(self, x, y):
        coords = []

        diag_x = x + 1
        diag_y = y + 1
        while diag_x <= self.max_x and diag_y <= self.max_y:
            coords.append((diag_x, diag_y))
            diag_x += 1
            diag_y += 1

        diag_x = x - 1
        diag_y = y - 1
        while diag_x > 0 and diag_y > 0:
            coords.append((diag_x, diag_y))
            diag_x -= 1
            diag_y -= 1

        return coords

    def get_banned_coordinates(self, queen_coordinates):
        banned_coordinates = set([queen_coordinates])
        queen_x, queen_y = queen_coordinates
        # all horizontals
        for x in range(1, self.max_x + 1):
            banned_coordinates.add((x, queen_y))

        # all verticals
        for y in range(1, self.max_y + 1):
            banned_coordinates.add((queen_x, y))

        banned_coordinates.update(self.get_left_leaning_diagonals(queen_x, queen_y))
        banned_coordinates.update(self.get_right_leaning_diagonals(queen_x, queen_y))

        return banned_coordinates


    def _solve(self, n, queen_coordinates, banned_coordinates):
        # all queens have been placed and none of them conflict
        if n == 0:
            return queen_coordinates

        viable_coordinates_set = self.all_coordinates() - banned_coordinates

        for viable_coordinates in viable_coordinates_set:
            new_banned_coordinates = self.get_banned_coordinates(viable_coordinates)
            result = self._solve(
                n - 1,
                queen_coordinates + [viable_coordinates],
                banned_coordinates.union(new_banned_coordinates),
            )
            if len(result):
                return result

        return []


    def solve(self, n):
        return self._solve(n, [], set())

NQueensSolver(8, 8).solve(8)
