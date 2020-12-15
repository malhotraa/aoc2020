from collections import defaultdict

def nth_number(nums, stop):
    memory = defaultdict(list)
    for idx, num in enumerate(nums):
        memory[num].append(idx + 1)

    while len(nums) < stop:
        last_num = nums[-1]
        if len(memory[last_num]) < 2:
            nums.append(0)
            memory[0].append(len(nums))
        else:
            diff = memory[last_num][-1] - memory[last_num][-2]
            nums.append(diff)
            memory[diff].append(len(nums))
    
    return nums[-1]

inp = [2,20,0,4,1,17]
print("2020th number: ", nth_number(inp, 2020))
print("30000000 number: ", nth_number(inp, 30000000))