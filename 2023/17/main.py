import itertools

import networkx as nx


def crucible_graph(losses, turn_bounds):
    H, W = len(losses), len(losses[0])
    G = nx.DiGraph()

    G.add_node("src")
    G.add_node("dst")
    G.add_nodes_from(itertools.product(range(H), range(W), range(2)))

    for i in range(2):
        G.add_edge("src", (0, 0, i), weight=0)
        G.add_edge((H - 1, W - 1, i), "dst", weight=0)

    for x, y, mult in itertools.product(range(H), range(W), [-1, 1]):
        w = 0
        for dx in range(1, turn_bounds[1] + 1):
            z = x + (mult * dx)
            if not (0 <= z < H):
                break
            w += losses[z][y]
            if dx >= turn_bounds[0]:
                G.add_edge((x, y, 0), (z, y, 1), weight=w)

        w = 0
        for dy in range(1, turn_bounds[1] + 1):
            z = y + (mult * dy)
            if not (0 <= z < W):
                break
            w += losses[x][z]
            if dy >= turn_bounds[0]:
                G.add_edge((x, y, 1), (x, z, 0), weight=w)

    return G


def main(path):
    with open(path, "r") as f:
        losses = [list(map(int, row.strip())) for row in f.readlines()]

    # Part 1
    G = crucible_graph(losses, turn_bounds=(1, 3))
    print(nx.single_source_dijkstra(G, "src", "dst")[0])

    # Part 2
    G = crucible_graph(losses, turn_bounds=(4, 10))
    print(nx.single_source_dijkstra(G, "src", "dst")[0])


if __name__ == "__main__":
    print("Example:")
    main("example.txt")
    print("Input:")
    main("input.txt")
