from collections import defaultdict

with open('input.txt') as f:
    lines = f.read().split('\n')

def part1and2(lines):
    ingredients = set()
    allergens = set()
    foods = []

    for line in lines:
        ing, aller = line.split("(")
        ing = ing.strip().split()
        aller = list(map(lambda x: x.strip(), aller[aller.find(' '):-1].split(',')))
        ingredients.update(ing)
        allergens.update(aller)
        foods.append((ing, aller))

    aller_to_candidates = defaultdict(set)
    for aller in allergens:
        aller_to_candidates[aller].update(ingredients)

    for food in foods:
        ings_in_food, aller_in_food = food
        for aller in aller_in_food:
            aller_to_candidates[aller] = set(ings_in_food).intersection(aller_to_candidates[aller])
    
    ings_with_allergens = set()
    for aller, ings in aller_to_candidates.items():
        ings_with_allergens.update(ings)

    count = 0
    for food in foods:
        count += len(set(food[0]) - ings_with_allergens)

    ings_to_allergen = dict()
    while len(ings_to_allergen) < len(ings_with_allergens):
        for aller in aller_to_candidates.keys():
            aller_to_candidates[aller].difference_update(set(ings_to_allergen.keys()))

        for aller, candidates in aller_to_candidates.items():
            if len(candidates) == 1:
                ings_to_allergen[list(candidates)[0]] = aller

    aller_to_ings = dict((aller, ings) for ings, aller in ings_to_allergen.items())
    res = []
    for aller in sorted(aller_to_ings.keys()):
        res.append(aller_to_ings[aller])
    
    return count, ",".join(res)  

print('part1:', part1and2(lines)[0])
print('part2:', part1and2(lines)[1])