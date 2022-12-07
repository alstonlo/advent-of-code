from __future__ import annotations

import collections
from dataclasses import dataclass
from typing import Optional, Dict


@dataclass
class Folder:

    parent: Optional[Folder]
    children: Dict[str, Folder]
    size: int = 0


def analyze_space_usage(path):
    with open(path, "r") as f:
        lines = [line.rstrip() for line in f.readlines()]
        buffer = collections.deque(lines)

    root = Folder(None, {})
    root.children["/"] = Folder(root, {})

    folders = [root.children["/"]]
    build_filesystem(buffer, root, folders)

    free_space = 70000000 - root.size
    folder_sizes = [folder.size for folder in folders]

    print("Part 1", sum(filter(lambda x: x <= 100000, folder_sizes)))
    print("Part 2", min(filter(lambda x: x + free_space >= 30000000, folder_sizes)))


def build_filesystem(buffer, root, registry):
    if not buffer:
        return

    cmd = buffer.popleft().split(" ")

    if cmd[1] == "cd":
        if cmd[2] == "..":
            root = root.parent
        else:
            root = root.children[cmd[2]]
    else:
        while buffer and not buffer[0].startswith("$"):
            info = buffer.popleft().split(" ")

            if info[0] == "dir":
                child = Folder(root, {})
                root.children[info[1]] = child
                registry.append(child)
            else:
                ancestor = root
                while ancestor is not None:
                    ancestor.size += int(info[0])
                    ancestor = ancestor.parent

    build_filesystem(buffer, root, registry)


if __name__ == "__main__":
    analyze_space_usage("terminal.txt")
