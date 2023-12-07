
with open('input') as f:
    lines = f.readlines()

total = 0

##amount = {
##    "red": 12,
##    "green": 13,
##    "blue": 14
##    }

for line in lines:
    line = line.replace('\n','')
    game = int(line.split(": ")[0].split(" ")[1])
    tries = line.split(": ")[1].split("; ")
    temp_amount = {
        "red": 0,
        "green": 0,
        "blue": 0
        }
    for i in range(len(tries)):
        tries[i] = tries[i].split(", ")
        for j in range(len(tries[i])):
            tries[i][j] = tries[i][j].split(" ")
            tries[i][j][0] = int(tries[i][j][0])
            if temp_amount[tries[i][j][1]] < tries[i][j][0]:
                temp_amount[tries[i][j][1]] = tries[i][j][0]
    res = temp_amount["red"] * temp_amount["green"] * temp_amount["blue"]
    total += res
print(total)

