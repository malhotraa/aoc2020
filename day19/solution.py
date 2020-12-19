import itertools
from collections import defaultdict

with open('input.txt') as f:
    rules, messages = f.read().split('\n\n')
    rules = rules.split('\n')
    messages = messages.split('\n')
    
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

def num_messages_matching_rule_0(rules, messages):
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
    
    num = 0
    for msg in messages:
        if msg in expanded_map['0']:
            num+=1
    return num

print('part1 :', num_messages_matching_rule_0(rules, messages))

