import re
with open('input.txt') as f:
    lines = f.read().split('\n')

def part1_evaluate_simple_expr(e):
    expr = e.strip('()').split()
    res = int(expr[0])
    op = None
    for i in range(1, len(expr)):
        if expr[i] in ['+', '*']:
            op = expr[i]
        else:
            if op == '+':
                res = res + int(expr[i])
            elif op == '*':
                res = res * int(expr[i])
            else:
                raise Exception('Op must be one of + or *')
    return res

def part1_evaluate(line):
    done = False
    while not done:
        matches = re.findall(r'\([^\(\)]*\)', line)
        if len(matches) == 0:
            return part1_evaluate_simple_expr(line)
        for match in matches:
            line = line.replace(match, str(part1_evaluate_simple_expr(match)))
        done = line.find('+') == -1 and line.find('*') == -1 and line.find('(') == -1 and line.find(')') == -1
    return int(line)

def part2_evaluate_simple_expr(e):
    e = e.strip('()')
    done = False
    while not done:
        matches = re.findall(r'(\d+ \+ \d+)', e)
        if len(matches) == 0:
            break
        for match in matches:
            a, op, b = match.split(' ')
            e = e.replace(match, str(int(a) + int(b)))
        done = e.find('+') == -1
    return eval(e)

def part2_evaluate(line):
    done = False
    while not done:
        matches = re.findall(r'\([^\(\)]*\)', line)
        if len(matches) == 0:
            res = part2_evaluate_simple_expr(line)
            return res
        for match in matches:
            line = line.replace(match, str(part2_evaluate_simple_expr(match)))
        done = line.find('+') == -1 and line.find('*') == -1 and line.find('(') == -1 and line.find(')') == -1

def part1_homework_sum(lines):
    return sum(list(map(part1_evaluate, lines)))

def part2_homework_sum(lines):
    return sum(list(map(part2_evaluate, lines)))

print('part1 homework_sum: ', part1_homework_sum(lines))
print('part2_homework_sum: ', part2_homework_sum(lines))
