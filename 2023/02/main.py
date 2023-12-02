from math import prod

Q1_BOUND = {"red": 12, "green": 13, "blue": 14}


def main():
    ans1 = 0
    ans2 = 0

    with open("input.txt", "r") as f:
        for row in f.readlines():
            title, games = row.strip().split(": ")

            bound = {c: 0 for c in Q1_BOUND}
            for outcome in games.split("; "):
                for count in outcome.split(", "):
                    num, c = count.split(" ")
                    bound[c] = max(bound[c], int(num))

            if all(v <= Q1_BOUND[k] for k, v in bound.items()):
                game_id = int(title.split(" ")[1])
                ans1 += game_id
            ans2 += prod(bound.values())

    print(ans1)
    print(ans2)


if __name__ == "__main__":
    main()
