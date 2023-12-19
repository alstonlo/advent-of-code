import math
import re


def shard_interval(I, num, le):
    num = int(num)

    # Too lazy to do smart interval slicing
    P, F = [], []
    for i in range(I[0], I[1] + 1):
        passes = (i < num) if le else (i > num)
        if passes:
            P.append(i)
        else:
            F.append(i)
    # So that I = Y + N

    # Convert back to (min, max)
    P = (min(P), max(P)) if P else None
    F = (min(F), max(F)) if F else None

    return P, F


def shard_bounds(comparison, bounds):
    bounds_pass = dict(bounds)
    bounds_fail = dict(bounds)

    k, num = re.split("<|>", comparison)
    Y, N = shard_interval(bounds[k], num=num, le=("<" in comparison))
    bounds_pass[k] = Y
    bounds_fail[k] = N

    return bounds_pass, bounds_fail


def num_accepted(R, name, bounds):
    if None in bounds.values():  # empty bounds
        return 0
    elif name == "R":
        return 0
    elif name == "A":
        return math.prod((r - l + 1) for l, r in bounds.values())
    else:
        count = 0
        for r in R[name][:-1]:
            comparison, out = r.split(":")
            shard, bounds = shard_bounds(comparison, bounds)
            count += num_accepted(R, out, shard)
            if None in bounds.values():
                break
        return count + num_accepted(R, R[name][-1], bounds)


def main(path):
    R = dict()
    parts = []

    with open(path, "r") as f:
        tokens = f.read().strip().split("\n\n")

        for row in tokens[0].split("\n"):
            name, rules, _ = re.split(r"{|}", row)
            R[name] = rules.split(",")

        for row in tokens[1].split("\n"):
            p = eval(f"dict({row[1:-1]})")
            parts.append(p)

    # Part 1
    ans1 = 0
    for p in parts:
        bounds = {k: (v, v) for k, v in p.items()}  # just to re-use part 2
        if num_accepted(R, "in", bounds) == 1:
            ans1 += sum(p.values())
    print(ans1)

    # Part 2
    bounds = {k: (1, 4000) for k in "xmas"}
    print(num_accepted(R, "in", bounds))


if __name__ == "__main__":
    print("Example:")
    main("example.txt")
    print("Input:")
    main("input.txt")
