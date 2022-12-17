import itertools


def parse_scan(path):
    scan = []

    with open(path, "r") as f:
        for line in f.readlines():
            tokens = line.strip().split(" ")
            name = tokens[1].strip()
            rate = int(tokens[4][:-1].replace("rate=", ""))
            adjs = [v.strip().replace(",", "") for v in tokens[9:]]
            scan.append((name, rate, adjs))

    # Valve name -> index in [0, N-1]
    labelling = {v: i for i, (v, _, _) in enumerate(scan)}
    N = len(labelling)

    flows = [0] * N
    tunnels = [[] for _ in range(N)]
    for name, rate, adjs in scan:
        u = labelling[name]
        flows[u] = rate
        for adj_name in adjs:
            tunnels[u].append(labelling[adj_name])
    return flows, tunnels, labelling["AA"]


def find_max_pressure_release(path):
    flows, tunnels, start = parse_scan(path)

    # ==============
    # Floyd Warshall
    # ==============

    N = len(flows)
    D = [[1e10] * N for _ in range(N)]  # pairwise shortest path lengths
    for u in range(N):
        D[u][u] = 0
    for u, adjs in enumerate(tunnels):
        for v in adjs:
            D[u][v] = 1
    for k, i, j in itertools.product(range(N), repeat=3):
        if D[i][j] > D[i][k] + D[k][j]:
            D[i][j] = D[i][k] + D[k][j]

    for u, v in itertools.product(range(N), repeat=2):
        if u == v:
            continue
        D[u][v] += 1  # add minute to turn on valve

    # ==================
    # Brute Force Search
    # ==================

    def _solve(src, valves, opened, t):
        score = 0

        for dst in valves:
            if (dst in opened) or (D[src][dst] >= t):
                continue

            t_next = t - D[src][dst]
            reward = flows[dst] * t_next

            opened.add(dst)
            value = reward + _solve(dst, valves, opened=opened, t=t_next)
            score = max(value, score)
            opened.remove(dst)

        return score

    working_valves = set(v for v in range(N) if flows[v] > 0)
    max_alone_release = _solve(start, working_valves, opened=set(), t=30)
    print("Part 1", max_alone_release)

    max_coop_release = 0
    for r in range(len(working_valves) // 2):
        for U in itertools.combinations(working_valves, r=r):
            U = set(U)
            max_coop_release = max(
                max_coop_release,
                sum(
                    _solve(start, valves, opened=set(), t=26)
                    for valves in [U, working_valves - U]
                )
            )
    print("Part 2", max_coop_release)


if __name__ == "__main__":
    find_max_pressure_release("valves.txt")
