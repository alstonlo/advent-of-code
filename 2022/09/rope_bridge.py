import numpy as np


# Implemented in NumPy for cleanness (originally written in pure Python)

AXIS_OFFSETS = np.asarray([[-1, 0], [1, 0], [0, 1], [0, -1]], dtype=np.int32)
DIAG_OFFSETS = np.asarray([[1, 1], [1, -1], [-1, 1], [-1, -1]], dtype=np.int32)

OFFSET_COMMANDS = {
    "L": AXIS_OFFSETS[0],
    "R": AXIS_OFFSETS[1],
    "U": AXIS_OFFSETS[2],
    "D": AXIS_OFFSETS[3],
}


def count_visited_tail_positions(path, part):
    assert part in {1, 2}
    L = 2 if (part == 1) else 10

    with open(path, "r") as f:
        motions = [line.rstrip().split(" ") for line in f.readlines()]

    visited = {(0, 0)}
    knots = np.zeros([L, 2], dtype=np.int32)

    for direction, num_steps in motions:
        for _ in range(int(num_steps)):
            knots[0] += OFFSET_COMMANDS[direction]

            for i, (prev, curr) in enumerate(zip(knots, knots[1:])):
                if np.abs(prev - curr).max() <= 1:
                    continue

                cands = curr[None, :] + (AXIS_OFFSETS if np.any(prev == curr) else DIAG_OFFSETS)
                dists = np.abs(cands - prev[None, :]).max(axis=1)
                knots[i + 1] = cands[np.argmin(dists)]

            visited.add(tuple(knots[-1]))

    print(f"Part {part}", len(visited))


if __name__ == "__main__":
    count_visited_tail_positions("motions.txt", part=1)
    count_visited_tail_positions("motions.txt", part=2)
