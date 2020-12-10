from collections import Counter
with open('input.txt') as f:
    nums = list(map(int, (f.read().split('\n'))))

def num_1_jolts_times_num_3_jolts(nums):
    nums = sorted(nums)
    nums.insert(0, 0)
    nums.append(nums[-1] + 3)
    diffs = [nums[i] - nums[i-1] for i in range(1, len(nums))]
    c = Counter(diffs)
    return c[1] * c[3]

def num_distinct_arrangements(nums):
    nums = sorted(nums)
    nums.insert(0, 0)
    nums.append(nums[-1] + 3)
    ways = [0] * len(nums)
    ways[0] = 1
    for i in range(1, len(nums)):
        for j in [1, 2, 3]:
            if i-j >= 0 and nums[i] - nums[i-j] <= 3:
                ways[i] += ways[i-j]
    return ways[-1]

print('num_1_jolts_times_num_3_jolts:', num_1_jolts_times_num_3_jolts(nums))
print('num_distinct_arrangements:', num_distinct_arrangements(nums))