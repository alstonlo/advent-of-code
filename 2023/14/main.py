import numpy as np


def north_load(grid):
    num_rocks = (grid == "O").sum(axis=1)
    return np.sum(num_rocks * np.arange(len(num_rocks), 0, -1))


def tilt_north(grid):
    is_O = (grid == "O")
    tilted = np.where(is_O, ".", grid)
    for i, j in zip(*np.nonzero(is_O)):
        k = i
        while (k > 0) and (tilted[k - 1, j] == "."):
            k -= 1
        tilted[k, j] = "O"
    return tilted


def main(path):
    with open(path, "r") as f:
        grid = np.array([list(row.strip()) for row in f.readlines()])

    # Part 1
    print(north_load(tilt_north(grid)))

    # Part 2
    N = 1000000000
    path = dict()

    for i in range(N):

        # One cycle
        grid = tilt_north(grid)  # tilt N
        grid = tilt_north(grid.T).T  # tilt W
        grid = tilt_north(grid[::-1])[::-1]  # tilt S
        grid = tilt_north(grid.T[::-1])[::-1].T  # tilt E

        # Represent as immutable string
        flat_grid = "".join(grid.flatten())

        if flat_grid in path:
            stem = path[flat_grid]
            end_id = stem + ((N - stem - 1) % (i - stem))
            end_grid = next(k for k, v in path.items() if v == end_id)
            end_grid = np.reshape(list(end_grid), grid.shape)
            print(north_load(end_grid))
            return

        else:
            path[flat_grid] = i


if __name__ == "__main__":
    print("Example:")
    main("example.txt")
    print("Input:")
    main("input.txt")
