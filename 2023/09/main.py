import re


def parse_int_list(s):
    s = s.strip()
    return list(map(int, re.split(r"\s+", s)))


def extrapolate(S, fwd=True):
    if len(set(S)) == 1:
        return S[0]
    diffs = [b - a for a, b in zip(S, S[1:])]
    inc = extrapolate(diffs, fwd=fwd)
    return (S[-1] + inc) if fwd else (S[0] - inc)


def main(path):
    with open(path, "r") as f:
        sequences = [parse_int_list(row) for row in f.readlines()]
    for fwd in [True, False]:
        print(sum(extrapolate(S, fwd) for S in sequences))


if __name__ == "__main__":
    print("Example:")
    main("example.txt")
    print("Input:")
    main("input.txt")
