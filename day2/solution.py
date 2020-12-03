import re
from collections import Counter

with open('input.txt') as f:
    lines = f.read().split("\n")

def part1(lines):
    valid_count = 0
    for line in lines:
        m = re.match(r"(\d+)\-(\d+)\ ([a-z]{1}):\ ([a-z]*)", line)
        min_, max_, char, passwd = m.group(1, 2, 3, 4)
        min_, max_ = int(min_), int(max_)
        freq = Counter(passwd)[char]
        if min_ <= freq <= max_:
            valid_count += 1
    return valid_count

def part2(lines):
    valid_count = 0
    for line in lines:
        m = re.match(r"(\d+)\-(\d+)\ ([a-z]{1}):\ ([a-z]*)", line)
        first, second, char, passwd = m.group(1, 2, 3, 4)
        first, second = int(first), int(second)
        is_valid = (passwd[first-1] == char and passwd[second-1] != char) \
                    or (passwd[first-1] != char and passwd[second-1] == char)
        if is_valid:
            valid_count += 1
    return valid_count


print(part1(lines))
print(part2(lines))
