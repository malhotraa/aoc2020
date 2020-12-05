with open('input.txt') as f:
    lines = f.read().split("\n")

def binary_search(seq, lo, hi, low_char):
    for c in seq:
        if c == low_char:
            hi = (lo + hi) // 2
        else:
            lo = ((lo + hi) // 2) + 1
    assert lo == hi
    return lo

def seat_id(seq):
    row = binary_search(seq[:7], 0, 127, 'F')
    col = binary_search(seq[7:], 0, 7, 'L')
    return row * 8 + col

def highest_seat_id(lines):
    return max(map(seat_id, lines))

def my_seat_id(lines):
    seats = sorted(map(seat_id, lines))
    for idx, seat in enumerate(seats):
        if idx > 0 and seat != seats[idx-1] + 1:
            return seat - 1

print(highest_seat_id(lines))
print(my_seat_id(lines))