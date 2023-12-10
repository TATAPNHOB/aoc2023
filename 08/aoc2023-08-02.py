from math import gcd
with open('input') as f:
    lines = f.readlines()

instructions = lines.pop(0).strip()

network = {}

current = []

for line in lines:
    line = line.strip()
    if line != "":
        line = line.split(" ")
        left_node = line[2].replace('(','').replace(',','')
        right_node = line[3].replace(')', '')
        network[line[0]] = {"left": left_node, "right": right_node}
        if (line[0][-1] == 'A'):
            current.append(line[0])


z_arrivings = [-1 for i in range(len(current))]

def z_found(arrivings):
    for i in range(len(arrivings)):
        if arrivings[i] == -1:
            return False
    return True

i = 0
while not z_found(z_arrivings):
    for rule in instructions:
        i += 1
        for j in range(len(current)):
            if rule == 'R':
                current[j] = network[current[j]]['right']
            elif rule == 'L':
                current[j] = network[current[j]]['left']
            if current[j][-1] == 'Z':
                z_arrivings[j] = i
        
        if not z_found(z_arrivings):
            break

print(z_arrivings)
lcm = 1
for q in z_arrivings:
    lcm = lcm * q // gcd(lcm, q)
print(lcm)