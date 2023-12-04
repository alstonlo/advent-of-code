import re


def parse_int_set(s):
    s = s.strip()
    return set(map(int, re.split(r"\s+", s)))


def main(path):
    num_matches = []
    with open(path, "r") as f:
        for row in f.readlines():
            win, have = row.strip().split(": ")[1].split("|")
            matches = parse_int_set(win) & parse_int_set(have)
            num_matches.append(len(matches))
    ans1 = sum((2 ** (m - 1)) for m in num_matches if (m > 0))

    N = len(num_matches)
    num_cards = [1] * N
    for i in range(N):
        for j in range(i + 1, i + num_matches[i] + 1):
            if j < N:
                num_cards[j] += num_cards[i]
    ans2 = sum(num_cards)

    print(ans1)
    print(ans2)


if __name__ == "__main__":
    print("Example:")
    main("example.txt")
    print("Input:")
    main("input.txt")
