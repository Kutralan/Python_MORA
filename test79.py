START = (2, 0)
EXIT = (11, 13)

# Each cell stores the directions you can move from that cell.
# N = North, E = East, S = South, W = West
maze = [
    ["ES",  "EW",  "ESW", "W",   "ES",  "EW",  "SW",  "E",   "ESW", "EW",  "W",   "ES",  "EW",  "SW"],
    ["NS",  "E",   "NEW", "W",   "NS",  "E",   "NEW", "ESW", "NSW", "E",   "EW",  "NEW", "W",   "NS"],
    ["NES", "ESW", "W",   "ES",  "NW",  "ES",  "W",   "NS",  "NE",  "EW",  "EW",  "SW",  "ES",  "NSW"],
    ["NS",  "NS",  "ES",  "NESW","EW",  "NW",  "E",   "NEW", "W",   "ES",  "EW",  "NW",  "NS",  "NS"],
    ["NS",  "NS",  "NS",  "NS",  "ES",  "EW",  "EW",  "SW",  "ES",  "NW",  "ES",  "EW",  "NW",  "NS"],
    ["NS",  "NS",  "N",   "NS",  "NS",  "ES",  "W",   "NS",  "NS",  "ES",  "NSW", "ES",  "SW",  "N"],
    ["N",   "NES", "SW",  "NS",  "NS",  "NS",  "ES",  "NEW", "NW",  "NS",  "NS",  "NS",  "NS",  "S"],
    ["S",   "NS",  "NS",  "NS",  "NS",  "NS",  "NES", "W",   "S",   "N",   "NES", "NW",  "NS",  "NS"],
    ["NS",  "N",   "NES", "NW",  "NS",  "NE",  "NW",  "ES",  "NW",  "S",   "NS",  "ES",  "NEW", "NSW"],
    ["NES", "EW",  "NEW", "W",   "NE",  "EW",  "SW",  "NE",  "EW",  "NEW", "NSW", "NS",  "S",   "NS"],
    ["N",   "S",   "ES",  "EW",  "EW",  "SW",  "NES", "SW",  "ES",  "EW",  "NW",  "NS",  "NS",  "NS"],
    ["ES",  "NSW", "NS",  "ES",  "SW",  "NE",  "NW",  "NS",  "NE",  "EW",  "SW",  "NS",  "NE",  "NW"],
    ["NS",  "NE",  "NW",  "NS",  "NE",  "ESW", "W",   "N",   "ES",  "EW",  "NW",  "NE",  "W",   "S"],
    ["NE",  "EW",  "EW",  "NEW", "W",   "NE",  "EW",  "EW",  "NEW", "EW",  "EW",  "EW",  "EW",  "NW"],
]

directions = [
    ("North", "N", -1, 0),
    ("East",  "E",  0, 1),
    ("South", "S",  1, 0),
    ("West",  "W",  0, -1),
]


def solve():
    stack = [START]
    visited = {START}
    moves = []

    print(f"Start at ( {START[0]} , {START[1]} )")

    while stack:
        row, col = stack[-1]

        if (row, col) == EXIT:
            if moves:
                print(f"{' '.join(moves)} Leaving at ( {row} , {col} )")
            else:
                print(f"Leaving at ( {row} , {col} )")
            return

        moved = False

        for word, symbol, dr, dc in directions:
            nr = row + dr
            nc = col + dc

            if (
                symbol in maze[row][col]
                and 0 <= nr < 14
                and 0 <= nc < 14
                and (nr, nc) not in visited
            ):
                stack.append((nr, nc))
                visited.add((nr, nc))
                moves.append(word)
                moved = True
                break

        if not moved:
            if moves:
                print(f"{' '.join(moves)} Stuck at ( {row} , {col} )")
                moves = []
            else:
                print(f"Stuck at ( {row} , {col} )")

            stack.pop()

            if stack:
                back_row, back_col = stack[-1]
                print(f"Back to ( {back_row} , {back_col} )")


solve()
