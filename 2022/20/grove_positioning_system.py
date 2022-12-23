def mixing(encryption, n_mixes):
    D = list(enumerate(encryption))  # input can contain duplicate numbers
    order = list(D)  # snapshot order
    for _ in range(n_mixes):
        for num in order:
            i = D.index(num)
            D.pop(i)
            i = (i + num[1]) % len(D)  # D here is one element shorter!
            D.insert(i, num)
    return [num[1] for num in D]


def decrypt_coordinates(path, part):
    assert part in {1, 2}

    with open(path, "r") as f:
        key = 1 if (part == 1) else 811589153
        encryption = [key * int(x) for x in f.readlines()]

    D = mixing(encryption, n_mixes=(1 if (part == 1) else 10))
    i0 = D.index(0)
    coords = [D[(i0 + 1000 * j) % len(D)] for j in range(1, 4)]
    print(f"Part {part}", sum(coords))


if __name__ == "__main__":
    decrypt_coordinates("encryption.txt", part=1)
    decrypt_coordinates("encryption.txt", part=2)
