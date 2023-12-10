import itertools

import numpy as np


PIPES = {"|": "NS", "-": "EW", "L": "NE", "J": "NW", "7": "SW", "F": "SE"}
DIRECTIONS = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}
PIPES = {k: [DIRECTIONS[d] for d in v] for k, v in PIPES.items()}
del DIRECTIONS


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


def pipe_ends(pipe, pos):
    if pipe not in PIPES:
        return []
    return [(pos[0] + i, pos[1] + j) for i, j in PIPES[pipe]]


def find_loop(grid, S):
    stems = []
    for pos, pipe in neighborhood(grid, S):
        for adj in pipe_ends(pipe, pos):
            if read(grid, adj) == "S":
                stems.append(pos)
    assert len(stems) == 2
    src, dst = stems  # arbitrarily label as src and dst

    path = [S, src]
    while path[-1] != dst:
        pos = path[-1]
        for adj in pipe_ends(read(grid, pos), pos):
            if adj != path[-2]:
                path.append(adj)
                break
        else:
            raise ValueError()
    return path


def bfs(marked):
    Q = [(0, 0)]  # sufficient due to border around grid
    write(marked, (0, 0), True)
    while Q:
        pos = Q.pop(0)
        for adj, m in neighborhood(marked, pos):
            if not m:
                write(marked, adj, True)
                Q.append(adj)


def main(path):
    with open(path, "r") as f:
        grid = [list(row.strip()) for row in f.readlines()]
    grid = np.array(grid)
    grid = np.pad(grid, ((1, 1), (1, 1)), constant_values=".")

    # Find loop
    S = tuple(idx.item() for idx in np.where(grid == "S"))
    loop = find_loop(grid, S)
    print(len(loop) // 2)

    # Find inner regions
    # Basic idea:
    #  - Create a 2x resolution grid marking points on the loop
    #  - Use flood fill (BFS) to mark areas outside the grid
    H, W = grid.shape
    marked = np.full([2 * H, 2 * W], False, dtype=bool)  # 2x resolution
    for pos in loop:
        pipe = read(grid, pos)
        pos = (pos[0] * 2, pos[1] * 2)
        write(marked, pos, True)
        for end in pipe_ends(pipe, pos):
            write(marked, end, True)
    bfs(marked)
    marked = marked[::2, ::2]  # downsample
    print((~marked).astype(int).sum())


if __name__ == "__main__":
    print("Example:")
    main("example.txt")
    print("Input:")
    main("input.txt")
