with open('input.txt') as f:
    lines = f.read().split("\n")

def accum_value(lines):
    pc = 0
    acc = 0
    visited = set()
    path = []
    while pc not in visited and pc >=0 and pc < len(lines):
        visited.add(pc)
        path.append(pc)
        instruction, value_str = lines[pc].split(' ')
        value = int(value_str)
        offset = 1
        if instruction == 'acc':
            acc += value
        elif instruction == 'jmp':
            offset = value
        pc += offset
    return acc, path, pc in visited

def fixed_program_accum_value(lines):
    _, path, _ = accum_value(lines)
    for i in range(len(path) - 1, -1, -1):
        orig_line = lines[path[i]]
        instruction, value_str = lines[path[i]].split(' ')
        if instruction == 'acc':
            continue
        lines[path[i]] = "{} {}".format('nop' if instruction == 'jmp' else 'jmp', value_str)
        acc, path, infinite_loop = accum_value(lines)
        if not infinite_loop:
            return acc
        lines[path[i]] = orig_line
    
    return None

print("Part 1:", accum_value(lines)[0])
print("Part 2:", fixed_program_accum_value(lines))