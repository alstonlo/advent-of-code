import collections
import sys

sys.setrecursionlimit(15000)


def beam(grid, x, y, vx, vy, seen):
    if not ((0 <= x < len(grid)) and (0 <= y < len(grid[0]))):  # out of bounds
        return
    if (vx, vy) in seen[(x, y)]:  # cycle
        return
    seen[(x, y)].add((vx, vy))

    tile = grid[x][y]
    if (tile == "-") and (vy == 0):
        new_vs = [(0, 1), (0, -1)]
    elif (tile == "|") and (vx == 0):
        new_vs = [(1, 0), (-1, 0)]
    elif tile in "/\\":
        d = -1 if (tile == "/") else 1
        new_vs = [(vy * d, vx * d)]
    else:
        new_vs = [(vx, vy)]
    for nvx, nvy in new_vs:
        beam(grid, x + nvx, y + nvy, nvx, nvy, seen)


def num_energized(grid, x, y, vx, vy):
    seen = collections.defaultdict(set)
    beam(grid, x, y, vx, vy, seen)
    return sum(1 for D in seen.values() if D)


def main(path):
    with open(path, "r") as f:
        grid = [list(row.strip()) for row in f.readlines()]

    # Part 1
    print(num_energized(grid, 0, 0, 0, 1))

    # Part 2
    E = []
    for i in range(len(grid)):
        E.append(num_energized(grid, i, 0, 0, 1))
        E.append(num_energized(grid, i, len(grid[0]) - 1, 0, -1))
    for i in range(len(grid[0])):
        E.append(num_energized(grid, 0, i, 1, 0))
        E.append(num_energized(grid, len(grid) - 1, i, -1, 0))
    print(max(E))


if __name__ == "__main__":
    print("Example:")
    main("example.txt")
    print("Input:")
    main("input.txt")
