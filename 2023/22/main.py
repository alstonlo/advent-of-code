from collections import defaultdict

import networkx as nx


def brick_coords(p, q):
    for i, (pi, qi) in enumerate(zip(p, q)):
        if pi != qi:
            brick = set()
            template = list(p)
            for k in range(min(pi, qi), max(pi, qi) + 1):
                template[i] = k
                brick.add(tuple(template))
            return brick
    return {p}


def height(brick):
    return min(z for _, _, z in brick)


def shiftz(brick, dz=0):
    return {(x, y, z + dz) for x, y, z in brick}


def main(path):
    snapshot = []
    with open(path, "r") as f:
        for row in f.readlines():
            ends = [tuple(map(int, b.split(","))) for b in row.strip().split("~")]
            snapshot.append(brick_coords(*ends))
    snapshot.sort(key=height)
    N = len(snapshot)

    # Simulate falling
    occupied = defaultdict(dict)

    # Construct graph, where i->j is an edge if brick j is stabilized by brick i
    G = nx.DiGraph()
    G.add_node("ground")
    G.add_nodes_from(range(N))

    for i, brick in enumerate(snapshot):
        while (height(brick) > 0) and not (occupied.keys() & brick):
            brick = shiftz(brick, dz=-1)
        for j in {occupied[p] for p in brick if p in occupied}:
            G.add_edge(j, i)
        if height(brick) == 0:
            G.add_edge("ground", i)
        brick = shiftz(brick, dz=1)
        occupied.update({p: i for p in brick})

    # Compute answers
    ans1 = 0
    ans2 = 0
    for node in range(N):
        H = G.copy()
        H.remove_node(node)
        reachable = nx.single_source_shortest_path(H, "ground")
        num_fall = len(snapshot) - len(reachable)
        ans1 += 1 if (num_fall == 0) else 0
        ans2 += num_fall
    print(ans1)
    print(ans2)


if __name__ == "__main__":
    print("Example:")
    main("example.txt")
    print("Input:")
    main("input.txt")
