import copy

with open('input.txt') as f:
    deck1, deck2 = f.read().split('\n\n')
    deck1 = list(map(int, deck1.split('\n')[1:]))
    deck2 = list(map(int, deck2.split('\n')[1:]))

def part1(deck1, deck2):
    while not (len(deck1) == 0 or len(deck2) == 0):
        a, b = deck1.pop(0), deck2.pop(0)
        if a > b:
            deck1.extend([a, b])
        else:
            deck2.extend([b, a])
    
    if len(deck1) > 0:
        return sum(deck1[i] * (len(deck1)-i) for i in range(len(deck1)))
    else:
        return sum(deck2[i] * (len(deck2)-i) for i in range(len(deck2)))

def recursive_combat(deck1, deck2):
    rounds = set()
    while not (len(deck1) == 0 or len(deck2) == 0):
        round_ = (tuple(deck1), tuple(deck2))
        # Infinite recursion rule
        if round_ in rounds:
            return 'p1', deck1

        rounds.add(round_)
        a, b = deck1.pop(0), deck2.pop(0)
        
        # Sub game rule
        if len(deck1) >= a and len(deck2) >= b:
            winner, _ = recursive_combat(copy.copy(deck1[:a]), copy.copy(deck2[:b]))  
        elif a > b:
            winner = 'p1'
        elif b > a:
            winner = 'p2'
        
        if winner == 'p1':
            deck1.extend([a, b])
        else:
            deck2.extend([b, a])
    
    if len(deck1) > 0:
        return 'p1', deck1

    elif len(deck2) > 0:
        return 'p2', deck2
    
def part2(deck1, deck2):
    winner, deck = recursive_combat(deck1, deck2)
    return sum(deck[i] * (len(deck)-i) for i in range(len(deck)))

print('part1:', part1(copy.copy(deck1), copy.copy(deck2)))
print('part2:', part2(copy.copy(deck1), copy.copy(deck2)))