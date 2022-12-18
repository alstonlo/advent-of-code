import itertools

import numpy as np


def neighbors(p):
    I = np.eye(3, dtype=np.int32)
    return tuple((p + sign * I[i]) for i, sign in itertools.product(range(3), [-1, 1]))


def simulate_falling_rocks(path):
    centers = []
    with open(path, "r") as f:
        for line in f.readlines():
            loc = [int(x) for x in line.strip().split(",")]
            centers.append(loc)
    centers = np.asarray(centers, dtype=np.int32)

    bounds = centers.max(axis=0) + 10
    lava = np.zeros(bounds, dtype=bool)
    for p in centers:
        lava[tuple(p)] = True

    # ======
    # Part 1
    # ======

    surface = 0
    for p in centers:
        for n in neighbors(p):
            if not lava[tuple(n)]:
                surface += 1
    print("Part 1", surface)

    # ======
    # Part 2
    # ======

    exterior = np.zeros_like(lava)
    start = bounds - 1

    Q = [tuple(start)]
    exterior[tuple(start)] = True
    while Q:
        p = Q.pop(0)
        for n in neighbors(p):
            if np.any((n < 0) | (bounds <= n)) or lava[tuple(n)] or exterior[tuple(n)]:
                continue
            exterior[tuple(n)] = True
            Q.append(tuple(n))

    surface = 0
    for p in centers:
        for n in neighbors(p):
            if exterior[tuple(n)]:
                surface += 1
    print("Part 2", surface)


if __name__ == "__main__":
    simulate_falling_rocks("lava_positions.txt")
