import math


def calculate_monkey_business(part):
    assert part in {1, 2}
    num_rounds = 20 if (part == 1) else 10000

    # I was again too lazy to write parsing code, so I just hand-copied this from the
    # puzzle input. The i-th entry in MONKEY_INFO stores
    #   1) the worry levels of the i-th monkey's current items
    #   2) the i-th monkey's operations
    #   3) a tuple (p, j, k) which says the monkey will throw an item to
    #      the j-th monkey if the worry level is divisible by p and the k-th monkey
    #      otherwise

    MONKEY_INFO = [
        ([99, 67, 92, 61, 83, 64, 98], lambda old: old * 17, (3, 4, 2)),
        ([78, 74, 88, 89, 50], lambda old: old * 11, (5, 3, 5)),
        ([98, 91], lambda old: old + 4, (2, 6, 4)),
        ([59, 72, 94, 91, 79, 88, 94, 51], lambda old: old * old, (13, 0, 5)),
        ([95, 72, 78], lambda old: old + 7, (11, 7, 6)),
        ([76], lambda old: old + 8, (17, 0, 2)),
        ([69, 60, 53, 89, 71, 88], lambda old: old + 5, (19, 7, 1)),
        ([72, 54, 63, 80], lambda old: old + 3, (7, 1, 3)),
    ]

    LCM_TEST_WORRIES = math.lcm(*[m[-1][0] for m in MONKEY_INFO])

    # ======

    counts = [0] * len(MONKEY_INFO)

    for _ in range(num_rounds):
        for i, (items, op, (p, j, k)) in enumerate(MONKEY_INFO):
            while items:
                counts[i] += 1
                worry = items.pop(0)

                if part == 1:
                    worry = op(worry) // 3
                else:
                    # The key insight here is that all monkey operations are
                    # additions and multiplications, and use that
                    #   a + b (mod p) = (a (mod p) + b (mod p)) (mod p)
                    #   a * b (mod p) = (a (mod p) * b (mod p)) (mod p)
                    worry = op(worry % LCM_TEST_WORRIES) % LCM_TEST_WORRIES

                catcher = j if (worry % p == 0) else k
                MONKEY_INFO[catcher][0].append(worry)

    counts.sort(reverse=True)
    print(f"Part {part}", counts[0] * counts[1])


if __name__ == "__main__":
    calculate_monkey_business(part=1)
    calculate_monkey_business(part=2)
