import functools
import itertools


def read(arr, p):
    return arr[p[0]][p[1]]


def write(arr, p, val):
    arr[p[0]][p[1]] = val


def find_shortest_paths(path):
    with open(path, "r") as f:
        heightmap = [list(line.rstrip()) for line in f.readlines()]
        M, N = len(heightmap), len(heightmap[0])

    coord_iter = functools.partial(itertools.product, range(M), range(N))

    # To do part 2 efficiently, we work backwards and treat this problem
    # as a hill descending problem. That is, we go E -> S

    Q = set()
    src, dst = None, None
    for x in coord_iter():
        if read(heightmap, x) == "S":
            dst = x
            write(heightmap, x, "a")
        elif read(heightmap, x) == "E":
            src = x
            write(heightmap, x, "z")
        Q.add(x)

    # A terrible implementation of Dijkstra's algorithm :)

    dists = [[float("inf")] * N for _ in range(M)]
    write(dists, src, 0)

    while Q:
        _, u = min((read(dists, x), x) for x in Q)
        Q.remove(u)
        for offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            v = (u[0] + offset[0], u[1] + offset[1])
            if (
                (0 <= v[0] < M) and (0 <= v[1] < N)
                and ord(read(heightmap, u)) <= ord(read(heightmap, v)) + 1
                and (v in Q)
                and read(dists, u) + 1 < read(dists, v)
            ):
                write(dists, v, read(dists, u) + 1)

    print("Part 1", read(dists, dst))
    print("Part 2", min(read(dists, x) for x in coord_iter() if (read(heightmap, x) == "a")))


if __name__ == "__main__":
    find_shortest_paths("heightmap.txt")
