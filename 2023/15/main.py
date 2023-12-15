import collections
import re


def hash(S):
    h = 0
    for c in S:
        h = (17 * (h + ord(c))) % 256
    return h


def main(path):
    with open(path, "r") as f:
        commands = f.read().strip().split(",")

    # Part 1
    print(sum(map(hash, commands)))

    # Part 2
    boxes = collections.defaultdict(list)
    lenses = dict()

    for cmd in commands:
        label, f = re.split(r"=|-", cmd)
        if "=" in cmd:
            if label not in lenses:
                boxes[hash(label)].append(label)
            lenses[label] = int(f)
        else:
            if label in lenses:
                lenses.pop(label)
                boxes[hash(label)].remove(label)

    ans2 = 0
    for box, L in boxes.items():
        for slot, label in enumerate(L, 1):
            ans2 += (box + 1) * slot * lenses[label]
    print(ans2)


if __name__ == "__main__":
    print("Example:")
    main("example.txt")
    print("Input:")
    main("input.txt")
