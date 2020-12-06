from functools import reduce

with open('input.txt') as f:
    lines = f.read().split("\n\n")

def part1(lines):
    num_yes = 0
    for group in lines:
        chars = set()
        answers = chars.update(*group.split('\n'))
        num_yes += len(chars)
    return num_yes

def part2(lines):
    num_yes = 0
    for group in lines:
       all_yes = reduce(lambda a, b: a.intersection(b), map(set, group.split('\n')))
       num_yes += len(all_yes)
    return num_yes

print(part1(lines))
print(part2(lines))