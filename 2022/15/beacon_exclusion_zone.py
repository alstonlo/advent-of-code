import tqdm

from report import SENSOR_REPORTS, DISTRESS_BOUND


def maximal_disjoint_intervals(itvs):
    itvs = sorted(itvs)

    merged = [itvs[0]]
    for I in itvs[1:]:
        M = merged[-1]
        if M[0] <= I[0] <= M[1] + 1:
            union_MI = (min(M[0], I[0]), max(M[1], I[1]))
            merged[-1] = union_MI
        else:
            merged.append(I)
    return merged


def find_distress_beacon():
    for y in tqdm.trange(DISTRESS_BOUND + 1, desc="Sweeping"):
        swept_itvs = []
        for (sx, sy), (bx, by) in SENSOR_REPORTS:
            dist = abs(sx - bx) + abs(sy - by)
            margin = dist - abs(sy - y)
            if margin >= 0:
                swept_itvs.append((sx - margin, sx + margin))
            if by == y:
                swept_itvs.append((bx, bx))
        swept_itvs = maximal_disjoint_intervals(swept_itvs)

        if y == 2000000:
            count = sum((r - l + 1) for l, r in swept_itvs)
            count -= len(set(bx for _, (bx, by) in SENSOR_REPORTS if (by == y)))
            print("Part 1", count)

        # Here, I rely on the fact that the distress signal location can be
        # uniquely determined to simplify code

        distress_x = None
        for I in swept_itvs:
            for x in [I[0] - 1, I[1] + 1]:
                if 0 <= x <= DISTRESS_BOUND:
                    distress_x = x
        if distress_x is not None:
            print("Part 2", DISTRESS_BOUND * distress_x + y)
            return


if __name__ == "__main__":
    find_distress_beacon()
