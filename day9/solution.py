from collections import defaultdict
with open('input.txt') as f:
    numbers = list(map(int, f.read().split("\n")))

def find_invalid_num(numbers):
    start, end = 0, 25

    while end <= len(numbers):
        diff_set = set([numbers[end] - numbers[i] for i in range(start, end)])
        found = any([(numbers[i] in diff_set and numbers[end] - numbers[i] != numbers[i]) for i in range(start, end)])
        if not found:
            return numbers[end]
        end += 1

    return None

def encryption_weakness(invalid_num, numbers):
    start, end = 0, 1

    running_sum = numbers[0] + numbers[1]
    while start < end and end < len(numbers):
        if running_sum == invalid_num:
            return min(numbers[start:end+1]) + max(numbers[start:end+1])
        elif running_sum > invalid_num:
            running_sum = running_sum - numbers[start]
            start += 1
        elif running_sum < invalid_num:
            end += 1
            running_sum = running_sum + numbers[end]
        if start == end:
            end += 1
            running_sum = running_sum + numbers[end]
    return None
invalid_num = find_invalid_num(numbers)
print('Invalid num:', find_invalid_num(numbers))
print('Encryption weakness:', encryption_weakness(invalid_num, numbers))
