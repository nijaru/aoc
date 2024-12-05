import re


def main():
    with open("input.txt") as f:
        data = f.read()

    pattern = r"mul\s*\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)"
    active = True
    total = 0

    split_pattern = r"(do\(\)|don\'t\(\))"
    sections = re.split(split_pattern, data)

    for section in sections:
        if section == "do()":
            active = True
        elif section == "don't()":
            active = False
        else:
            if active:
                matches = re.findall(pattern, section)
                for a, b in matches:
                    product = int(a) * int(b)
                    total += product
    print(total)


if __name__ == "__main__":
    main()
