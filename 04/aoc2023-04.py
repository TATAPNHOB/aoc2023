with open('input') as f:
    lines = f.readlines()

total = 0

copies = [1 for i in range(len(lines))]

card = 0

for line in lines:
    n = 0
    line = line.replace('\n','')
    line = line.split(": ")[1]
    winning = line.split(" | ")[0].split(" ")
    your = line.split(" | ")[1].split(" ")
    while "" in winning:
        winning.remove("")
    while "" in your:
        your.remove("")
    for i in range(len(winning)):
        winning[i] = int(winning[i])
    for i in range(len(your)):
        your[i] = int(your[i])
    
    for win in winning:
        if win in your:
            n += 1
    for j in range(copies[card]):
        for i in range(card + 1, card + n + 1):
            if i < len(lines):
                copies[i] += 1
            else:
                print(card, i)
    card += 1
for copy in copies:
    total += copy
print(copies)
print(total)
    
