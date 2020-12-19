import copy
import itertools
from collections import defaultdict

def expand_rules(rid, rules_map, expanded_map):
    if rid in expanded_map:
        return
    if rid not in rules_map:
        raise Exception("Rule {} not found in rules map".format(rid))
    elif isinstance(rules_map[rid], list):
        for ids in rules_map[rid]:
            for id_ in ids:
                expand_rules(id_, rules_map, expanded_map)
            exp_set = expanded_map[ids[0]]
            for id_ in ids[1:]:
                curr_exp = expanded_map[id_]
                if exp_set is None or curr_exp is None:
                    print("rid {}, ids: {} {}, expansions: {} {}".format(rid, ids[0], ids[1], exp_set, curr_exp))
                prod = itertools.product(exp_set, curr_exp)
                prod = list(map(lambda t: t[0] + t[1], prod))
                exp_set = prod

            expanded_map[rid].update(exp_set)
    else:
        raise Exception("Unknown rule type for rule {}".format(rid))

    assert rid in expanded_map

with open('input.txt') as f:
    rules, messages = f.read().split('\n\n')
    rules = rules.split('\n')
    messages = messages.split('\n')

    rules_map = {}
    expanded_map = defaultdict(set)
    for rule in rules:
        idx, deps = rule.split(':')
        if '"' in deps:
            deps = deps.strip(' "')
            expanded_map[idx].add(deps)
        else:
            deps = deps.strip().split('|')
            deps = list(map(lambda x: x.split(), deps))
            rules_map[idx] = deps
    
    expand_rules('0', rules_map, expanded_map)

def part2_match(exp42, exp31, msg):
    msg_a, msg_b = copy.copy(msg), copy.copy(msg)
    num42 = 0
    num31 = 0
    done = False
    
    while not done:
        done = True
        for exp in exp42:
            if msg_a[:8] == exp:
                msg_a = msg_a[8:]
                num42 += 1
                done = False
                break

    done = False
    while not done:
        done = True
        for exp in exp31:
            if msg_b[-8:] == exp:
                msg_b = msg_b[:-8]
                num31 += 1
                done = False
                break

    if num42 == 0 or num31 == 0:
        return False

    for i in range(num42):
        for j in range(num31):
            if num42 > num31 and ((i+1) * 8 + (j+1) * 8) == len(msg):
                return True

    return False

def part1(expanded_map, messages):
    num = 0
    for msg in messages:
        if msg in expanded_map['0']:
            num+=1
    return num

def part2(expanded_map, messages):
    num = 0
    for msg in messages:
        if part2_match(expanded_map['42'], expanded_map['31'], msg):
            num+=1
    return num

print('part1 :', part1(expanded_map, messages))
print('part2 :', part2(expanded_map, messages))

