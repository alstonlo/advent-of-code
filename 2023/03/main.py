import collections
import itertools


def box_range(*bounds):
    return itertools.product(*[range(*b) for b in bounds])


def main(path):
    with open(path, "r") as f:
        engine = [list("." + row.strip() + ".") for row in f.readlines()]
    dots = ["."] * len(engine[0])
    engine.insert(0, dots)
    engine.append(dots)

    ans1 = 0
    gears = collections.defaultdict(list)
    num = ""

    for row, col in box_range([len(engine)], [len(engine[0])]):
        if engine[row][col].isdigit():
            num = num + engine[row][col]

        elif num:  # number finished
            part_found = False
            for i, j in box_range([row - 1, row + 2], [col - len(num) - 1, col + 1]):
                c = engine[i][j]
                if c.isdigit() or (c == "."):
                    continue
                part_found = True
                if c == "*":
                    gears[(i, j)].append(int(num))
            if part_found:
                ans1 += int(num)
            num = ""

    ans2 = sum(v[0] * v[1] for v in gears.values() if (len(v) == 2))

    print(ans1)
    print(ans2)


if __name__ == "__main__":
    print("Example:")
    main("example.txt")
    print("Input:")
    main("input.txt")
