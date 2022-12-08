def analyze_tree_heights(path):
    with open(path, "r") as f:
        heights = [[int(x) for x in line.rstrip()] for line in f.readlines()]

    num_visible = 0
    max_score = 0

    for r, row in enumerate(heights):
        for c, h in enumerate(row):
            all_views = all_views_from_tree(heights, r=r, c=c)

            # Boarder tree
            if not all(view for view in all_views):
                num_visible += 1
                continue

            # Interior tree
            if any(h > max(view) for view in all_views):
                num_visible += 1

            score = 1
            for view in all_views:
                num_seen = 0
                for k in view:
                    num_seen += 1
                    if k >= h:
                        break
                score *= num_seen
            max_score = max(max_score, score)

    print("Part 1", num_visible)
    print("Part 2", max_score)


def all_views_from_tree(heights, r, c):
    lview = heights[r][:c]
    rview = heights[r][c + 1:]
    uview = list(heights[i][c] for i in range(r))
    dview = list(heights[i][c] for i in range(r + 1, len(heights)))

    lview.reverse()
    uview.reverse()

    return [lview, rview, uview, dview]


if __name__ == "__main__":
    analyze_tree_heights("heights.txt")
