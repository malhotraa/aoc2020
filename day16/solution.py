import re

with open('input.txt') as f:
    lines = f.read().split('\n\n')
    rules_lines = lines[0].split('\n')
    your_tikt = lines[1].split('\n')[1]
    nearby_tikts = lines[2].split('\n')[1:]

    rules = {}
    for rule in rules_lines:
        name, cond = rule.split(':')
        m = re.match(r" (\d+)-(\d+) or (\d+)-(\d+)", cond)
        s1, e1, s2, e2 = m.group(1, 2, 3, 4)
        rules[name] = (int(s1), int(e1), int(s2), int(e2))

def is_invalid_num(num):
    for s1, e1, s2, e2 in rules.values():
        if (s1 <= num <= e1) or (s2 <= num <= e2):
            return False
    return True

def is_valid_ticket(tikt):
    nums = list(map(int, tikt.split(',')))
    nums = list(filter(is_invalid_num, nums))
    return len(nums) == 0

def possible_rules(tikts, field):
    possible = set()
    for name, rule in rules.items():
        valid = True
        for t in tikts:
            valid = valid and ((rule[0] <= t[field] <= rule[1]) or (rule[2] <= t[field] <= rule[3]))
        if valid:
            possible.add(name)
    return possible

def scanning_error_rate(rules, nearby_tikts):
    error_rate = 0
    for tikt in nearby_tikts:
        nums = list(map(int, tikt.split(',')))
        nums = list(filter(is_invalid_num, nums))
        error_rate += sum(nums)
    return error_rate

def departure_fields_product(rules, your_tikt, nearby_tikts):
    all_tikts = [your_tikt] + nearby_tikts
    valid_tikts = list(filter(is_valid_ticket, all_tikts))
    assert len(valid_tikts) > 0

    valid_tikts = list(map(lambda x: list(map(int, x.split(','))), valid_tikts))
    num_fields = len(valid_tikts[0])

    # Field idx to rule name
    assignment = {}
    while len(assignment) < num_fields:
        for idx in range(num_fields):
            possible_rules_ = list(possible_rules(valid_tikts, idx))
            if len(possible_rules_) == 1:
                name = possible_rules_[0]
                assignment[idx] = name
                rules.pop(name)

    your_tikt = list(map(int, your_tikt.split(',')))
    product = 1
    for idx, name in assignment.items():
        if name.startswith('departure'):
            product *= your_tikt[idx]
    return product

print('scanning_error_rate: ', scanning_error_rate(rules, nearby_tikts))
print('departure_fields_product: ', departure_fields_product(rules, your_tikt, nearby_tikts))