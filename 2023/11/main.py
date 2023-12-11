import itertools

import numpy as np


def main(path):
    with open(path, "r") as f:
        grid = [list(row.strip()) for row in f.readlines()]
    grid = np.array(grid)
    galaxies = list(zip(*np.where(grid == "#")))

    for expansion in [2, int(1e6)]:
        rw = np.where(np.any(grid == "#", axis=1), 1, expansion)
        cw = np.where(np.any(grid == "#", axis=0), 1, expansion)

        ans = 0
        for (gx, gy), (hx, hy) in itertools.combinations(galaxies, 2):
            sx = 1 if (hx >= gx) else -1
            sy = 1 if (hy >= gy) else -1
            ans += rw[gx:hx:sx].sum() + cw[gy:hy:sy].sum()
        print(ans)


if __name__ == "__main__":
    print("Example:")
    main("example.txt")
    print("Input:")
    main("input.txt")
