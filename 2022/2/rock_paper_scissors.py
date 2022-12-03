def outcome(my_move, op_move):
    if my_move == op_move:
        return 3  # draw
    elif op_move == (my_move + 1) % 3:
        return 0  # loss
    else:
        return 6  # win 


def evaluate_strategy(path, part):
    score = 0

    with open(path, "r") as f:
        for line in f.readlines():
            moves = line.rstrip().split(" ")

            op_move = ord(moves[0]) - ord("A")

            if part == 1:
                my_move = ord(moves[1]) - ord("X")
            elif part == 2:
                offset = ord(moves[1]) - ord("X") - 1
                my_move = (op_move + offset) % 3
            else:
                raise ValueError()

            score += outcome(my_move, op_move) + (my_move + 1)

    print(f"Part {part}", score)


if __name__ == "__main__":
    evaluate_strategy("guide.txt", part=1)
    evaluate_strategy("guide.txt", part=2)
