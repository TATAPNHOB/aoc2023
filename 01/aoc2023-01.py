
with open('input') as f:
    lines = f.readlines()

total = 0
accepted = '01234567890'
spells = {
    "zero": '0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
    }

inv_spells = {v: k for k, v in spells.items()}

for line in lines:
    num = ''
    line = line.replace('\n','')
    print(line, end=' ')
    i = 99999999
    w = ''
    for spell in list(spells) + list(accepted):
        if line.find(spell) != -1:
            if line.find(spell) < i:
                w = spell
                i = line.find(spell)
    if w in spells:
        first = spells[w]
    elif w in accepted:
        first = w
    i = -1
    w = ''
    for spell in list(spells) + list(accepted):
        if line.rfind(spell) != -1:
            if line.rfind(spell) > i:
                w = spell
                i = line.rfind(spell)
    if w in spells:
        last = spells[w]
    elif w in accepted:
        last = w
    for char in line:
        if char in accepted:
            num += char
    num = first + last
    num = int(num)
    total += num
    print(num)
print(total)
