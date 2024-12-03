def part1():
    with open("input.txt") as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            nums = [int(x) for x in line.split(" ")]

            if nums != sorted(nums) and nums != sorted(nums, reverse=True):
                continue

            if all(
                abs(nums[i] - nums[i - 1]) in [1, 2, 3] for i in range(1, len(nums))
            ):
                count += 1
        print(count)


def valid_diff(num1, num2):
    return abs(num1 - num2) in [1, 2, 3]


def is_valid_sequence(nums):
    if len(nums) < 2:
        return False

    is_ascending = nums[1] > nums[0]

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return False

        if is_ascending and nums[i] < nums[i - 1]:
            return False
        if not is_ascending and nums[i] > nums[i - 1]:
            return False

        if not valid_diff(nums[i], nums[i - 1]):
            return False

    return True


def part2():
    with open("input.txt") as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            nums = [int(x) for x in line.split()]

            if is_valid_sequence(nums):
                count += 1
                continue

            for i in range(len(nums)):
                test_nums = nums[:i] + nums[i + 1 :]
                if is_valid_sequence(test_nums):
                    count += 1
                    break

        print(count)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
