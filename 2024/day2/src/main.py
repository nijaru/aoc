def part1():
    with open("input.txt") as f:
        count = 0
        for line in f:
            nums = [int(x) for x in line.split(" ")]

            if nums != sorted(nums) and nums != sorted(nums, reverse=True):
                continue

            if all(
                abs(nums[i] - nums[i - 1]) in [1, 2, 3] for i in range(1, len(nums))
            ):
                count += 1
        print(count)


def is_valid_with_skip(nums, skip_idx=-1):
    if len(nums) - (1 if skip_idx >= 0 else 0) < 2:
        return False

    prev = None
    is_ascending = None

    for i in range(len(nums)):
        if i == skip_idx:
            continue
        if prev is None:
            prev = nums[i]
            continue

        diff = nums[i] - prev
        if abs(diff) > 3 or diff == 0:
            return False

        if is_ascending is None:
            is_ascending = diff > 0

        if (is_ascending and diff <= 0) or (not is_ascending and diff >= 0):
            return False

        prev = nums[i]

    return True


def part2():
    count = 0
    with open("input.txt") as f:
        for line in f:
            nums = [int(x) for x in line.split()]

            if is_valid_with_skip(nums):
                count += 1
                continue

            for i in range(len(nums)):
                if is_valid_with_skip(nums, i):
                    count += 1
                    break

    print(count)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
