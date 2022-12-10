import re


def simulate_procedure(path, part):
    assert part in {1, 2}

    # I was too lazy to write parsing code, so I just hand-copied this from the
    # puzzle input and deleted the corresponding lines
    crates = [
        list("SMRNWJVT"),
        list("BWDJQPCV"),
        list("BJFHDRP"),
        list("FRPBMND"),
        list("HVRPTB"),
        list("CBPT"),
        list("BJRPL"),
        list("NCSLTZBW"),
        list("LSG"),
    ]

    with open(path, "r") as f:
        for line in f.readlines():
            tokens = line.rstrip().split(" ")
            num = int(tokens[1])
            src = int(tokens[3]) - 1
            dst = int(tokens[5]) - 1

            moved = crates[src][-num:]
            crates[src] = crates[src][:-num]
            crates[dst].extend(moved if (part == 2) else reversed(moved))

    print(f"Part {part}", "".join(c[-1] for c in crates))


if __name__ == "__main__":
    simulate_procedure("procedure.txt", part=1)
    simulate_procedure("procedure.txt", part=2)
