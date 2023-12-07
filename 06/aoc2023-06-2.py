with open('input') as f:
    lines = f.readlines()

def record_beating_times(time, distance):
    total = 0
    for i in range(time):
        if (i * (time - i) > distance):
            total += 1
    return total

competitions = []

for line in lines:
    line = line.replace('\n','')
    line = line.replace(" ",'')
    print(line)
    competitions.append(list(map(int, line.split(":")[1].split(" "))))

print(competitions)

total = 1

for i in range(len(competitions[0])):
    t = record_beating_times(competitions[0][i], competitions[1][i])
    if t != 0:
        total *= t

print(total)
