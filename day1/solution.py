with open('input.txt') as f:
    numbers = map(int, f.read().split('\n')[:-1])

def _2sum(numbers):
    s = set(numbers)
    for i in numbers:
        if (2020-i) in s:
            return i * (2020-i)
    return None

print(_2sum(numbers))

def _3sum(numbers):
    s = set(numbers)
    for i, val_i in enumerate(numbers):
        for j, val_j in enumerate(numbers[i+1:]):
            to_find = (2020-val_i-val_j)
            if to_find in s and to_find not in [val_i, val_j]:
                return val_i * val_j * to_find

print(_3sum(numbers))
