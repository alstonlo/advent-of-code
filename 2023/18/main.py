import itertools

import numpy as np


# =========================================================================== #
#                             Copied from Day 10                              #
# =========================================================================== #


def read(grid, pos):
    return grid[pos[0], pos[1]]


def write(grid, pos, val):
    grid[pos[0], pos[1]] = val


def box_range(*bounds):
    return itertools.product(*[range(*b) for b in bounds])


def neighborhood(grid, pos):
    for nb in box_range(*[[pos[i] - 1, pos[i] + 2] for i in range(2)]):
        if (pos != nb) and all(0 <= nb[i] < grid.shape[i] for i in range(2)):
            yield nb, read(grid, nb)


def bfs(marked):
    Q = [(0, 0)]  # sufficient due to border around grid
    write(marked, (0, 0), True)
    while Q:
        pos = Q.pop(0)
        for adj, m in neighborhood(marked, pos):
            if not m:
                write(marked, adj, True)
                Q.append(adj)


# =========================================================================== #
#                                 Day 18 Code                                 #
# =========================================================================== #


def pairwise(L):
    return zip(L[:-1], L[1:])


def parse_dig_plan(path, part1):
    p = (0, 0)
    vertices = [p]

    with open(path, "r") as f:
        for row in f.readlines():
            tokens = row.strip().split(" ")
            if part1:
                direction = tokens[0]
                steps = int(tokens[1])
            else:
                hexcode = tokens[2][2:-1]
                direction = {"0": "R", "1": "D", "2": "L", "3": "U"}[hexcode[-1]]
                steps = int(hexcode[:-1], 16)

            if direction == "U":
                v = (-steps, 0)
            elif direction == "D":
                v = (+steps, 0)
            elif direction == "L":
                v = (0, -steps)
            else:
                v = (0, +steps)
            p = tuple(pi + vi for pi, vi in zip(p, v))  # move
            vertices.append(p)

    return vertices


def contracted_grid(vertices):
    xorder, yorder = [sorted(set(L)) for L in zip(*vertices)]

    H, W = (2 * len(xorder) - 1), (2 * len(yorder) - 1)
    contracted = np.full([H, W], False)
    for p, q in pairwise(vertices):
        (px, py), (qx, qy) = sorted([p, q])
        px = 2 * xorder.index(px)
        py = 2 * yorder.index(py)
        qx = 2 * xorder.index(qx)
        qy = 2 * yorder.index(qy)
        contracted[px:qx + 1, py:qy + 1] = True

    areas = np.ones([H, W], dtype=np.int64)
    for i, (x0, x1) in enumerate(pairwise(xorder)):
        areas[2 * i + 1, :] *= (x1 - x0 - 1)
    for i, (y0, y1) in enumerate(pairwise(yorder)):
        areas[:, 2 * i + 1] *= (y1 - y0 - 1)

    # Convenient to pad by 1
    padding = ((1, 1), (1, 1))
    contracted = np.pad(contracted, padding, constant_values=False)
    areas = np.pad(areas, padding, constant_values=0)

    return contracted, areas


def main(path, part1=True):
    vertices = parse_dig_plan(path, part1=part1)
    trench, areas = contracted_grid(vertices)

    exterior = np.copy(trench)
    bfs(exterior)
    interior = ~exterior | trench

    print(np.where(interior, areas, 0).sum().item())


if __name__ == "__main__":
    print("Example:")
    main("example.txt", part1=True)
    main("example.txt", part1=False)
    print("Input:")
    main("input.txt", part1=True)
    main("input.txt", part1=False)
