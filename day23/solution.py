import time

class Node:
    def __init__(self, data, next_ = None):
        self.data = data
        self.next = next_
    
    def __repr__(self):
        return "Node({})".format(self.data)

class CircularLinkedList:
    """Circular linked list with following properties:
        * O(1) insertion/removal time
        * O(1) min max retrieval time """
    def __init__(self, label):
        self.num_to_node = dict()
        self.min = self.max = first_val = int(label[0])
        self.head = curr = Node(first_val)
        self.num_to_node[first_val] = self.head
        for i in range(1, len(label)):
            val = int(label[i])
            self.min = min(self.min, val)
            self.max = max(self.max, val)
            curr.next = Node(int(label[i]))
            self.num_to_node[int(label[i])] = curr.next
            curr = curr.next
        curr.next = self.head

    def add(self, node, at): # O(1)
        self.num_to_node[node.data] = node
        insert_node = self.num_to_node[at]
        node.next = insert_node.next
        insert_node.next = node
        self.min = min(self.min, node.data)
        self.max = max(self.max, node.data)

    def traverse(self, start = None):
        if start is None:
            start = self.head
        curr = start
        while curr is not None and curr.next != start:
            yield curr
            curr = curr.next
        yield curr

    def find(self, data): # O(1)
        return self.num_to_node[data]

    def minmax(self): # O(1)
        return self.min, self.max

    def pick3(self, node): # O(1)
        prev = node
        picked = []
        for node in self.traverse(node.next):
            if self.head == node:
                self.head = node.next
            picked.append(node)
            self.num_to_node.pop(node.data)
            if len(picked) == 3:
                prev.next = node.next
                while self.min in [picked[0].data, picked[1].data, picked[2].data]:
                    self.min += 1
                while self.max in [picked[0].data, picked[1].data, picked[2].data]:
                    self.max -= 1
                return picked

    def add3(self, nodes, at): # O(1)
        insert_node = self.num_to_node[at]
        nodes[2].next = insert_node.next
        insert_node.next = nodes[0]
        for node in nodes:
            self.num_to_node[node.data] = node
            self.min = min(self.min, node.data)
            self.max = max(self.max, node.data)

    def __repr__(self):
        nodes = []
        for node in self.traverse():
            nodes.append(str(node.data))
        return ','.join(nodes)


def run_sim(label, total_moves, add_mil = False):
    ll = CircularLinkedList(label)
    
    if add_mil:
        _, max_val = ll.minmax()
        prev = ll.find(int(label[-1])).data
        for i in range(max_val + 1, 1000001):
            ll.add(Node(i), prev)
            prev = i

    curr = ll.head
    for move in range(total_moves):
        cup = curr.data
        picked = ll.pick3(curr)
        picked_nums = set([picked[0].data, picked[1].data, picked[2].data])

        min_val, max_val = ll.minmax()
        dest = cup - 1 if cup - 1 >= min_val else max_val
        while dest in picked_nums:
            dest -= 1
            if dest < min_val:
                dest = max_val

        ll.add3(picked, dest)
        curr = curr.next

    return ll

def part1(label, total_moves):
    ll = run_sim(label, total_moves)
    nodes = []
    for node in ll.traverse(ll.find(1)):
        nodes.append(str(node.data))
    return ''.join(nodes)[1:]

def part2(label, total_moves):
    ll = run_sim(label, total_moves, True)
    node_1 = ll.find(1)
    return node_1.next.data * node_1.next.next.data

print('part1:', part1('157623984', 100))
print('part2:', part2('157623984', 10000000))
