import operator

OPERATION_REGISTRY = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
    "=": operator.eq,
}


class Monkey:

    def __init__(self):
        self.listeners = []
        self.listening = []
        self.op = None
        self.num = None

    def yell(self):
        if any((monkey.num is None) for monkey in self.listening):  # not ready to yell
            return

        if self.num is None:
            operands = [self.listening[0].num, self.listening[1].num]
            if any((x == "?") for x in operands):
                self.num = "?"
            else:
                self.num = OPERATION_REGISTRY[self.op](*operands)

        for monkey in self.listeners:
            monkey.yell()

    def deduce(self):
        if (self.num == "?") or (not self.listening):
            return
        operands = [self.listening[0].num, self.listening[1].num]
        if operands.count("?") != 1:  # cannot deduce
            return

        missing_idx = operands.index("?")
        child = self.listening[missing_idx]
        given = operands[1 - missing_idx]

        if self.op == "=":
            child.num = given
        elif self.op == "+":
            child.num = self.num - given
        elif self.op == "-":
            if missing_idx == 0:
                child.num = self.num + given
            else:
                child.num = given - self.num
        elif self.op == "*":
            child.num = self.num // given
        else:
            if missing_idx == 0:
                child.num = self.num * given
            else:
                child.num = given // self.num

        child.deduce()


def parse_monkey_jobs(path):
    with open(path, "r") as f:
        monkey_jobs = [line.strip().split(": ") for line in f.readlines()]

    tribe = {name: Monkey() for name, _ in monkey_jobs}
    number_monkeys = []
    human = None

    for name, job in monkey_jobs:
        monkey = tribe[name]
        if job.isnumeric():
            monkey.num = int(job)
            number_monkeys.append(monkey)
        else:
            a, op, b = job.split(" ")
            monkey.op = op
            monkey.listening = [tribe[a], tribe[b]]
            tribe[a].listeners.append(monkey)
            tribe[b].listeners.append(monkey)
        if name == "humn":
            human = monkey

    return tribe, number_monkeys, human


def simulate_monkeys_yelling(path):

    # ======
    # Part 1
    # ======

    tribe, number_monkeys, _ = parse_monkey_jobs(path)
    for monkey in number_monkeys:
        monkey.yell()
    print("Part 1", tribe["root"].num)

    # ======
    # Part 2
    # ======

    tribe, number_monkeys, human = parse_monkey_jobs(path)

    tribe["root"].op = "="
    tribe["root"].num = True
    human.num = "?"

    for monkey in number_monkeys:
        monkey.yell()
    tribe["root"].deduce()

    print("Part 2", human.num)


if __name__ == "__main__":
    simulate_monkeys_yelling("monkey_jobs.txt")
