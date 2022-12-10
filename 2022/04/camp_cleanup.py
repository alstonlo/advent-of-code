import re


def count_overlap(path):
    n_contain = 0
    n_overlap = 0

    with open(path, "r") as f:
        for line in f.readlines():
            line = line.rstrip()
            amin, amax, bmin, bmax = [int(token) for token in re.split(r",|-", line)]

            # This is extremely slow compared to case enumeration but was fast to write
            arange = set(range(amin, amax + 1))
            brange = set(range(bmin, bmax + 1))

            if (arange <= brange) or (brange <= arange):
                n_contain += 1
            if arange & brange:
                n_overlap += 1

    print("Part 1", n_contain)
    print("Part 2", n_overlap)


if __name__ == "__main__":
    count_overlap("assignments.txt")
