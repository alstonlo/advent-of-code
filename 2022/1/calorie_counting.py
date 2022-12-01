def count_calories(path):
    counts = [0]

    with open(path) as f:
        for line in f.readlines():
            line = line.rstrip()
            if line == "":
                counts.append(0)
            else:
                counts[-1] += int(line)

    counts.sort(reverse=True)

    print("Part 1", counts[0])
    print("Part 2", sum(counts[:3]))


if __name__ == "__main__":
    count_calories("calories.txt")
