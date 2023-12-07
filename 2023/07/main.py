COMBO_RANKINGS = {
    (5,): 6,
    (1, 4): 5,
    (2, 3): 4,
    (1, 1, 3): 3,
    (1, 2, 2): 2,
    (1, 1, 1, 2): 1,
    (1, 1, 1, 1, 1): 0
}

CARD_RANKINGS = {c: i for i, c in enumerate(reversed("AKQJT98765432"))}


def rank(hand, part1):
    counts = {c: hand.count(c) for c in set(hand)}

    # Part 2 idea: it's always optimal to turn J into the highest frequency card
    if (not part1) and (len(counts) > 1):
        J = counts.pop("J", 0)
        counts[max(counts, key=counts.get)] += J

    # Rank hand
    counts = tuple(sorted(counts.values()))
    combo = COMBO_RANKINGS[counts]
    tie = [(CARD_RANKINGS[c] if (part1 or (c != "J")) else -1) for c in hand]

    return combo, tie


def main(path, part1):
    hands, bids = [], {}

    with open(path, "r") as f:
        for row in f.readlines():
            hand, bid = row.split(" ")
            hands.append(hand)
            bids[hand] = int(bid)

    hands.sort(key=lambda h: rank(h, part1))
    print(sum(i * bids[h] for i, h in enumerate(hands, 1)))


if __name__ == "__main__":
    print("Example:")
    main("example.txt", part1=True)
    main("example.txt", part1=False)
    print("Input:")
    main("input.txt", part1=True)
    main("input.txt", part1=False)
