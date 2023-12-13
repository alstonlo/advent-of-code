import numpy as np


def score(grid, tol):
    for G, mult in [(grid, 100), (grid.T, 1)]:
        for i in range(1, G.shape[0]):
            margin = min(i, G.shape[0] - i)
            window = G[(i - margin):(i + margin)]
            if np.sum(window != window[::-1]) == tol:
                return i * mult
    raise ValueError()


def main(path):
    with open(path, "r") as f:
        grids = [
            np.array([list(row) for row in chunk.split("\n")])
            for chunk in f.read().strip().split("\n\n")
        ]
    print(sum(score(grid, tol=0) for grid in grids))
    print(sum(score(grid, tol=2) for grid in grids))


if __name__ == "__main__":
    print("Example:")
    main("example.txt")
    print("Input:")
    main("input.txt")
