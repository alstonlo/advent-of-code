def working(S):
    return set(S) <= set(".?")


def broken(S):
    return set(S) <= set("#?")


def arrangements(S, groups):
    S = "." + S  # simplifies logic
    L, G = len(S), len(groups)

    # Dynamic programming
    dp = [[0] * L for _ in range(G)]
    for i in range(G):
        for j in range(1, L):
            l, r = (j - groups[i] + 1), (j + 1)
            if working(S[j]):
                dp[i][j] += dp[i][j - 1]
            if (l >= 0) and broken(S[l:r]) and working(S[l - 1:l]):
                if i == 0:
                    dp[i][j] += int(working(S[:l]))
                else:
                    dp[i][j] += dp[i - 1][l - 2] if (l >= 2) else 0
    return dp[-1][-1]


def main(path):
    ans1 = 0
    ans2 = 0
    with open(path, "r") as f:
        for row in f.readlines():
            S, groups = row.strip().split(" ")
            groups = tuple(map(int, groups.split(",")))
            ans1 += arrangements(S, groups)
            ans2 += arrangements("?".join([S] * 5), groups * 5)
    print(ans1)
    print(ans2)


if __name__ == "__main__":
    print("Example:")
    main("example.txt")
    print("Input:")
    main("input.txt")
