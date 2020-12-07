from collections import defaultdict
import re

with open('input.txt') as f:
    lines = f.read().split("\n")

def bags_containing_atleast_one_shiny_gold_bag(lines):
    # Build map of bag -> set of bags that can contain it
    bag_to_container = defaultdict(set)
    for line in lines:
        container_bag, rest = line.split(' bags contain')
        n_contained_bags = re.findall(r"(\d+ [a-z]+ [a-z]+) bag", rest)
        for n_contained_bag in n_contained_bags:
            n = int(n_contained_bag[0])
            contained_bag = n_contained_bag[2:]
            bag_to_container[contained_bag].add(container_bag)
    
    shiny_gold_containers = set()
    to_explore = bag_to_container['shiny gold']
    while len(to_explore):
        bag = to_explore.pop()
        shiny_gold_containers.add(bag)
        to_explore.update(bag_to_container[bag])
    return len(shiny_gold_containers)

def num_bags_in_bag(bag_to_contained, bag):
    if bag not in bag_to_contained:
        raise Exception("Bag {} not found in bag_to_contained map".format(bag))
    if len(bag_to_contained[bag]) == 0:
        return 0
    num_bags = 0
    for (n, contained_bag) in bag_to_contained[bag]:
        num_bags += (n + n * num_bags_in_bag(bag_to_contained, contained_bag))
    return num_bags

def bags_in_shiny_gold_bag(lines):
    # Build map of bag -> set of bags contained
    bag_to_contained = defaultdict(list)
    for line in lines:
        container_bag, rest = line.split(' bags contain')
        bag_to_contained[container_bag] = []
        n_contained_bags = re.findall(r"(\d+ [a-z]+ [a-z]+) bag", rest)
        for n_contained_bag in n_contained_bags:
            n = int(n_contained_bag[0])
            contained_bag = n_contained_bag[2:]
            bag_to_contained[container_bag].append((n, contained_bag))
    return num_bags_in_bag(bag_to_contained, 'shiny gold')

print(bags_containing_atleast_one_shiny_gold_bag(lines))
print(bags_in_shiny_gold_bag(lines))