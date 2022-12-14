def drop_sand_unit(obstacles, H):
    if (500, 0) in obstacles:
        return False

    x = 500
    for y in range(H):
        for offset in [0, -1, 1]:
            if (x + offset, y + 1) not in obstacles:
                x = x + offset
                break
        else:
            obstacles.add((x, y))
            return True
    return False


def simulate_falling_sand(path, part):
    assert part in {1, 2}

    obstacles = set()
    D = 0

    with open(path, "r") as f:
        for line in f.readlines():
            path = []

            for coord in line.rstrip().split(" -> "):
                coord = coord.split(",")
                coord = tuple(map(int, coord))

                path.append(coord)
                D = max(D, coord[1])

            for (xl, yl), (xr, yr) in zip(path, path[1:]):
                if xl == xr:
                    start, end = min(yl, yr), max(yl, yr)
                    obstacles |= {(xl, y) for y in range(start, end + 1)}
                else:
                    start, end = min(xl, xr), max(xl, xr)
                    obstacles |= {(x, yl) for x in range(start, end + 1)}

    D += 2

    # Note that sand can only ever rest within a rectangular region whose
    # apex is at (500, 0) and base at depth d is width 2d - 1. Since
    # D = 168, this triangle contains roughly 1 + 3 + ... + 2H - 1 = D^2 ~ 28k
    # sand particles, so we can also brute force the simulation

    if part == 2:
        obstacles |= {(x + 500, D) for x in range(-2 * D - 10, 2 * D + 11)}

    num_resting = 0
    while drop_sand_unit(obstacles, H=D):
        num_resting += 1
    print(f"Part {part}", num_resting)


if __name__ == "__main__":
    simulate_falling_sand("scan.txt", part=1)
    simulate_falling_sand("scan.txt", part=2)
