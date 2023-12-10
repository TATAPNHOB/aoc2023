
with open('input') as f:
    lines = f.readlines()

total = 0

def is_zeroes(list):
    for i in list:
        if i != 0:
            return False
    return True

for line in lines:
    line = line.strip()
    values = line.split(' ')
    values = [[int(values[i]) for i in range(len(values))]]
    while not is_zeroes(values[-1]):
        values.append([])
        for i in range(len(values[-2]) - 1):
            values[-1].append(values[-2][i + 1] - values[-2][i])
    t = 0
    for i in range(2, len(values) + 1):
        t = t + values[-i][-1]
    print(t)
    total += t
print(total)
    