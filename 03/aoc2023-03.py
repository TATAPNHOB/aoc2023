
digits = '01234567890'

def is_symbol(char):
    return char not in digits and char != "."

def is_digit(char):
    return char in digits

def is_symbolled(i, j, grid):
    top =  is_symbol(grid[i - 1][j - 1]) or is_symbol(grid[i - 1][j]) or is_symbol(grid[i - 1][j + 1])
    middle = is_symbol(grid[i][j - 1]) or is_symbol(grid[i][j + 1])
    bottom = is_symbol(grid[i + 1][j - 1]) or is_symbol(grid[i + 1][j]) or is_symbol(grid[i + 1][j + 1])
    return top or middle or bottom

def number(i, j, grid):
    if not is_digit(grid[i][j]):
        return ""
    else:
        return number_left(i, j - 1, grid) + grid[i][j] + number_right(i, j + 1, grid) 

def number_left(i, j, grid):
    if not is_digit(grid[i][j]):
        return ""
    else:
        return number_left(i, j - 1, grid) + grid[i][j]

def number_right(i, j, grid):
    if not is_digit(grid[i][j]):
        return ""
    else:
        return grid[i][j] + number_right(i, j + 1, grid)



def gear_check(i, j, grid):
    numbers = []
    numbers.append(number(i, j - 1, grid))
    numbers.append(number(i, j + 1, grid))
    if is_digit(grid[i - 1][j]):
        numbers.append(number(i - 1, j, grid))
    else:
        numbers.append(number(i - 1, j - 1, grid))
        numbers.append(number(i - 1, j + 1, grid))

    if is_digit(grid[i + 1][j]):
        numbers.append(number(i + 1, j, grid))
    else:
        numbers.append(number(i + 1, j - 1, grid))
        numbers.append(number(i + 1, j + 1, grid))
    
    real_numbers = []
    for n in numbers:
        if not (n == ""):
            real_numbers.append(int(n))
    if len(real_numbers) == 2:
        return real_numbers[0] * real_numbers[1]
    else:
        return 0
with open('input') as f:
    lines = f.readlines()
    
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n','')

lines.insert(0, "." * len(lines[0]))
lines.insert(len(lines), "." * len(lines[0]))

for i in range(len(lines)):
    lines[i] = "." + lines[i] + "."

total = 0

##for i in range(1, len(lines) - 1):
##    num = ''
##    digit_mode = False
##    symbol_around = False
##    for j in range(1, len(lines[i]) - 1):
##        if lines[i][j] in digits:
##            digit_mode = True
##            num += lines[i][j]
##            if (is_symbolled(i, j, lines)):
##                symbol_around = True
##        else:
##            if digit_mode:
##                if symbol_around:
##                    print(num)
##                    digit_mode = False
##                    total += int(num)
##                    num = ''
##                    symbol_around = False
##            digit_mode = False
##            num = ''
##            symbol_around = False
##    if digit_mode:
##        if symbol_around:
##            digit_mode = False
##            total += int(num)

for i in range(1, len(lines) - 1):
    for j in range(1, len(lines[i]) -1):
        if lines[i][j] == "*":
            total += gear_check(i, j, lines)
                
print(total)
