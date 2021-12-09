inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

numOnes = 0
numFours = 0
numSevens = 0
numEights = 0

for entry in inp:
    digitWires, entryDisplay = entry.split(' | ')
    digitWireSplit = digitWires.split()
    for digit in digitWireSplit:
        if len(digit) == 2:
            numOnes += 1
        elif len(digit) == 4:
            numFours += 1
        elif len(digit) == 3:
            numSevens += 1
        elif len(digit) == 7:
            numEights += 1

print(numOnes + numFours + numSevens + numEights)
