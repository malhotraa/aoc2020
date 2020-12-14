import re

with open('input.txt') as f:
    lines = f.read().split('\n')

def apply_mask_v1(mask, value):
    value_str = format(value, '036b')
    assert len(mask) == len(value_str)
    mod_value = ''
    for i in range(len(mask)):
        if mask[i] != 'X':
            mod_value += mask[i]
        else:
            mod_value += value_str[i]  
    return int(mod_value, 2)

def sum_memory_v1(lines):
    memory = {}
    idx = 0
    while idx < len(lines):
        if re.search('mask = ', lines[idx]):
            mask = lines[idx][len('mask = '):]
            idx += 1
            while idx < len(lines) and not re.search('mask = ', lines[idx]):
                m = re.match(r'mem\[(\d+)\] = (\d+)', lines[idx])
                addr, value = m.group(1, 2)
                memory[addr] = apply_mask_v1(mask, int(value))
                idx += 1
    return sum(memory.values())

def apply_mask_v2(mask, addr):
    addr_str = format(addr, '036b')
    assert len(mask) == len(addr_str)
    floating_addr = ''
    floating_idxs = []
    for i in range(len(mask)):
        if mask[i] == 'X':
            floating_addr += mask[i]
            floating_idxs.append(i)
        elif mask[i] == '0':
            floating_addr += addr_str[i]
        elif mask[i] == '1':
            floating_addr += '1'
        else:
            raise Exception("Unknown mask bit type {}".format(mask[i]))

    addrs = []
    for i in range(2**len(floating_idxs)):
        bin_i = format(i, '0{}b'.format(len(floating_idxs)))
        temp_addr = []
        k = 0
        for j in range(len(floating_addr)):
            if floating_addr[j] != 'X':
                temp_addr.append(floating_addr[j])
            else:
                temp_addr.append(bin_i[k])
                k += 1
        temp_addr = ''.join(temp_addr)
        addrs.append(int(temp_addr, 2))
    return addrs

def sum_memory_v2(lines):
    memory = {}
    idx = 0
    while idx < len(lines):
        if re.search('mask = ', lines[idx]):
            mask = lines[idx][len('mask = '):]
            idx += 1
            while idx < len(lines) and not re.search('mask = ', lines[idx]):
                m = re.match(r'mem\[(\d+)\] = (\d+)', lines[idx])
                addr, value = m.group(1, 2)
                for addr_ in apply_mask_v2(mask, int(addr)):
                    memory[addr_] = int(value)
                idx += 1
    return sum(memory.values())

print('sum_memory_v1: ', sum_memory_v1(lines))
print('sum_memory_v2: ', sum_memory_v2(lines))


