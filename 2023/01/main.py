DIGITS = {  # comment out to solve part 1
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
for d in range(1, 10):
    DIGITS[str(d)] = d


def main():
    ans = 0
    with open("input.txt", "r") as f:
        for s in f.readlines():
            ld = min(DIGITS, key=lambda d: s.find(d) if (s.find(d) >= 0) else len(s))
            rd = max(DIGITS, key=lambda d: s.rfind(d))
            ans += 10 * DIGITS[ld] + DIGITS[rd]
    print(ans)


if __name__ == "__main__":
    main()
