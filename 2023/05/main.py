import re


def parse_int_list(s):
    s = s.strip()
    return list(map(int, re.split(r"\s+", s)))


def main(path, part1):
    with open(path, "r") as f:
        seeds = f.readline()
        almanac = f.read()

    seeds = parse_int_list(seeds.split(": ")[-1])
    if part1:
        seeds = [(n, n) for n in seeds]
    else:
        seeds = [(n, n + inc - 1) for n, inc in zip(seeds[::2], seeds[1::2])]

    # Basic idea:
    # - Each mapping is a step function
    # - Such functions map sets of intervals to sets of intervals
    itvs = seeds

    for mapping in almanac.split("\n\n"):
        mapping = mapping.split(":\n")[-1].split("\n")
        mapping = map(parse_int_list, mapping)
        mapping = sorted(mapping, key=lambda v: v[1])

        itvs_image = []

        for I in itvs:

            for ys, xs, xinc in mapping:
                X = (xs, xs + xinc - 1)

                # Find overlap of X & I
                O = (max(X[0], I[0]), min(X[1], I[1]))
                if O[0] > O[1]:  # no overlap
                    continue
                L = (I[0], O[0] - 1)  # might be empty
                R = (O[1] + 1, I[1])  # might be empty
                # So that I = O + L + R

                # Overlap gets mapped
                itvs_image.append(tuple(ys + O[i] - xs for i in range(2)))

                if L[0] <= L[1]:
                    itvs_image.append(L)  # we sorted mapping, so L is fixed
                if R[0] <= R[1]:
                    I = R
                else:
                    break  # no more interval left
            else:
                itvs_image.append(I)

        itvs = itvs_image

    print(min(I[0] for I in itvs))


if __name__ == "__main__":
    print("Example:")
    main("example.txt", part1=True)
    main("example.txt", part1=False)
    print("Input:")
    main("input.txt", part1=True)
    main("input.txt", part1=False)
