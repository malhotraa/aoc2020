
def part1(sub_number, card_pub_key, door_pub_key):
    card_loop_size = 0
    start = 1
    while start != card_pub_key:
        start = (start * sub_number) % 20201227
        card_loop_size += 1
    door_loop_size = 0
    start = 1
    while start != door_pub_key:
        start = (start * sub_number) % 20201227
        door_loop_size += 1
    start = 1
    for _ in range(card_loop_size):
        start = (start * door_pub_key) % 20201227
    return start

print('part1:', part1(7, 14205034, 18047856))