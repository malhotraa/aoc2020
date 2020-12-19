from functools import partial

with open('input.txt') as f:
    lines = f.read().split('\n')

def par1_precedence(op):
    return 1

def part2_precedence(op):
    if op == '+':
        return 1
    elif op == '*':
        return 0
    else:
        raise Exception("Unsupported op {}".format(op))

def evaluate(precedence_fn, expr):
    ops = []
    values = []
    i = 0
    while i < len(expr):
        if expr[i] == ' ':
            pass
        elif expr[i] == '(':
            ops.append(expr[i])
        elif expr[i].isdigit():
            start = i
            while i < len(expr) and expr[i].isdigit():
                i +=1
            values.append(int(expr[start:i]))
            i -= 1
        elif expr[i] == ')':
            # Pop stacks and eval expression
            while len(ops) > 0 and ops[-1] != '(':
                op = ops.pop()
                a = values.pop()
                b = values.pop()
                values.append(eval("{}{}{}".format(a, op, b)))
            ops.pop()
        elif expr[i] in ['*', '+']:
            while len(ops) > 0 and ops[-1] != '(' and precedence_fn(ops[-1]) >= precedence_fn(expr[i]):
                op = ops.pop()
                a = values.pop()
                b = values.pop()
                values.append(eval("{}{}{}".format(a, op, b)))
            ops.append(expr[i])
        else:
            raise Exception("Unknown item {}".format(expr[i]))
        i += 1

    while len(ops) > 0:
        op = ops.pop()
        a = values.pop()
        b = values.pop()
        values.append(eval("{}{}{}".format(a, op, b)))
    
    assert len(ops) == 0 and len(values) == 1
    return values[0]

def part1_homework_sum(lines):
    return sum(list(map(partial(evaluate, par1_precedence), lines)))

def part2_homework_sum(lines):
    return sum(list(map(partial(evaluate, part2_precedence), lines)))

print('part1 homework_sum: ', part1_homework_sum(lines))
print('part2_homework_sum: ', part2_homework_sum(lines))
