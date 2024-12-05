def part1():
    with open("input.txt") as f:
        nums = zip(*[map(int, line.split()) for line in f])
        a, b = map(sorted, nums)
        print(sum(abs(x - y) for x, y in zip(a, b)))


def part2():
    with open("input.txt") as f:
        nums = zip(*[map(int, line.split()) for line in f])
        a, b = map(sorted, nums)
        print(sum(x * b.count(x) for x in a if x in b))


def main():
    part1()
