import math
import re


def parse_int_list(s):
    s = s.strip()
    return list(map(int, re.split(r"\s+", s)))


def main(path, part1):
    with open(path, "r") as f:
        read_fn = lambda: f.readline() if part1 else f.readline().replace(" ", "")
        times = parse_int_list(read_fn().split(":")[-1])
        dists = parse_int_list(read_fn().split(":")[-1])

    # Basic idea:
    # - The distance travelled is quadratic w.r.t the time the button pressed
    # - Solve for the roots
    # - Compute the length of the largest integer interval strictly between them
    ans = 1
    for T, D in zip(times, dists):
        discr = math.sqrt((T ** 2) - 4 * D)
        lo = (T - discr) / 2
        hi = (T + discr) / 2
        ans *= math.ceil(hi - 1) - math.floor(lo + 1) + 1
    print(ans)


if __name__ == "__main__":
    print("Example:")
    main("example.txt", part1=True)
    main("example.txt", part1=False)
    print("Input:")
    main("input.txt", part1=True)
    main("input.txt", part1=False)
