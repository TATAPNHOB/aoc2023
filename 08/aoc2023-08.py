
with open('input') as f:
    lines = f.readlines()

instructions = lines.pop(0).strip()

network = {}

for line in lines:
    line = line.strip()
    if line != "":
        line = line.split(" ")
        left_node = line[2].replace('(','').replace(',','')
        right_node = line[3].replace(')', '')
        network[line[0]] = {"left": left_node, "right": right_node}

i = 0

current = 'AAA'
while current != 'ZZZ':
    for rule in instructions:
        i += 1
        if rule == 'R':
            current = network[current]['right']
        elif rule == 'L':
            current = network[current]['left']
        
        if current == 'ZZZ':
            break

print(i)