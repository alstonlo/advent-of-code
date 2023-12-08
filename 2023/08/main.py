import itertools
import math


def parse_input(path):
    G = dict()
    with open(path, "r") as f:
        moves = f.readline().strip()
        f.readline()
        for row in f.readlines():
            src, dsts = row.strip().split(" = ")
            G[src] = tuple(dsts[1:-1].split(", "))
    return G, moves


def main1(path):
    G, moves = parse_input(path)

    v = "AAA"
    for step, d in enumerate(itertools.cycle(moves), 1):
        v = G[v][int(d == "R")]
        if v == "ZZZ":
            print(step)
            return


def main2(path):
    G, moves = parse_input(path)

    cycle_sizes = []

    for v in G:
        if not v.endswith("A"):
            continue

        path, visited = [v], {v: 0}

        for step, d in enumerate(itertools.cycle(moves), 1):
            dst = G[path[-1]][int(d == "R")]

            if dst not in visited:
                visited[dst] = step

            elif (step - visited[dst]) % len(moves) == 0:
                path = [v[-1] for v in path]  # only suffix matters

                # Here, we've found a cycle. The path will look like
                # v1, v2, ..., vm -> [some infinite cycle]:
                m = visited[dst]
                cycle = path[m:]

                # Conveniently, each path crosses exactly one destination node,
                # which is contained in the cycle. Call this node D.
                assert (path[:m].count("Z") == 0) and (cycle.count("Z") == 1)

                # This is saying that the number of steps we take to reach
                # node D the first time is the same as if we were to traverse
                # a full cycle starting at D.
                assert (m + cycle.index("Z")) == len(cycle)

                # Together, we see that every len(cycle) steps, we reach
                # node D again, so the LCM expression below is correct.
                cycle_sizes.append(len(cycle))
                break

            path.append(dst)

    print(math.lcm(*cycle_sizes))


if __name__ == "__main__":
    print("Example:")
    main1("example.txt")
    print("Input:")
    main1("input.txt")
    main2("input.txt")
