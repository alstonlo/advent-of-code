def priority(letter):
    if letter.islower():
        return ord(letter) - ord("a") + 1
    else:
        return ord(letter) - ord("A") + 27


def calculate_rucksack_scores(path):
    with open(path, "r") as f:
        lines = [line.rstrip() for line in f.readlines()]

    score = 0
    for line in lines:
        n = len(line) // 2
        shared = set(line[:n]) & set(line[n:])
        letter = next(iter(shared))
        score += priority(letter)
    print("Part 1", score)

    score = 0
    for i in range(0, len(lines), 3):
        shared = set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2])
        letter = next(iter(shared))
        score += priority(letter)
    print("Part 2", score)


if __name__ == "__main__":
    calculate_rucksack_scores("rucksacks.txt")
