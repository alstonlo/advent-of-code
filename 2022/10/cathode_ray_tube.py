def sum_strength_and_draw_sprite(path):
    cycle = 1
    X = 1

    total_strength = [0]  # in a list so we can mutate in nested function
    sprite = [["."] * 40 for _ in range(6)]

    def update_strength_and_sprite():
        if cycle % 40 == 20:
            total_strength[0] += (cycle * X)
        row = (cycle - 1) // 40
        col = (cycle - 1) % 40
        sprite[row][col] = "#" if (abs(col - X) <= 1) else "."

    with open(path, "r") as f:
        instructions = [line.rstrip() for line in f.readlines()]

    for cmd in instructions:
        if cmd == "noop":
            update_strength_and_sprite()
            cycle += 1
        else:
            V = int(cmd.split(" ")[1])
            for _ in range(2):
                update_strength_and_sprite()
                cycle += 1
            X += V

    print("Part 1", total_strength[0])
    print("Part 2")
    print("\n".join("".join(pixel for pixel in row) for row in sprite))


if __name__ == "__main__":
    sum_strength_and_draw_sprite("instructions.txt")
