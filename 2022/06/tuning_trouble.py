def find_start_marker(path, part):
    assert part in {1, 2}
    w = 4 if (part == 1) else 14

    with open(path, "r") as f:
        buffer = f.read().rstrip()

    for i in range(len(buffer) - w + 1):
        window = buffer[i: i + w]
        if len(set(window)) == w:
            print(f"Part {part}", i + w)
            return


if __name__ == "__main__":
    find_start_marker("buffer.txt", part=1)
    find_start_marker("buffer.txt", part=2)
