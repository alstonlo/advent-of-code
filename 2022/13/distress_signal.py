from functools import cmp_to_key

from packets import PACKETS, DIVIDERS


def compare(a, b):
    if type(a) is type(b):
        if isinstance(a, int):
            if a == b:
                return 0
            return -1 if (a < b) else 1
        else:
            for items in zip(a, b):
                order = compare(*items)
                if order == 0:
                    continue
                else:
                    return order
            return compare(len(a), len(b))
    else:
        if isinstance(a, int):
            return compare([a], b)
        else:
            return compare(a, [b])


def analyze_packets():
    num_right_order = 0
    for i, pair in enumerate(zip(*[iter(PACKETS)] * 2)):
        if compare(*pair) == -1:
            num_right_order += (i + 1)
    print("Part 1", num_right_order)

    key = 1
    for i, s in enumerate(sorted(PACKETS + DIVIDERS, key=cmp_to_key(compare))):
        if s in DIVIDERS:
            key *= (i + 1)
    print("Part 2", key)


if __name__ == "__main__":
    analyze_packets()
