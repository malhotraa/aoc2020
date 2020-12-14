import math
from functools import reduce

with open('input.txt') as f:
    lines = f.read().split('\n')

def earliest_bus(lines):
    earliest_time = int(lines[0])
    buses = list(map(int, filter(lambda id_: id_ != 'x', lines[1].split(','))))
    min_bus = buses[0]
    min_time = None
    for bus_id in buses:
        time_diff = int(math.ceil(earliest_time / bus_id) * bus_id - earliest_time)
        if min_time is None:
            min_time = time_diff
        elif time_diff < min_time:
            min_time = time_diff
            min_bus = bus_id
    return min_bus * min_time

# Find smallest t such that
# 41x = t
# (41x + 35) % 37 == 0 (x=19)
# (41x + 14) % 29 == 0

def earliest_timestamp_offsets(lines):
    items = lines[1].split(',')
    buses = []
    offsets = []
    for idx, item in enumerate(items):
        if item != 'x':
            buses.append(int(item))
            offsets.append(idx % int(item))
    product = buses[0]
    start = buses[0]
    for i in range(1, len(buses)):
        while (start + offsets[i]) % buses[i] != 0:
            start = start + product
        product *= buses[i]
    return start

print('earliest_bus:', earliest_bus(lines))
print('earliest_timestamp_offsets:', earliest_timestamp_offsets(lines))