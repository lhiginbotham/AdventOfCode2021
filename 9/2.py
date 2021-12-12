inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

rowCount = len(inp)
colCount = len(inp[0])

lowPoints = []
lowPointVals = []
for row in range(rowCount):
    for col in range(colCount):
        curVal = int(inp[row][col])
        
        # top
        if row > 0 and int(inp[row - 1][col]) <= curVal:
            continue
        # bottom
        if row < rowCount - 1 and int(inp[row + 1][col]) <= curVal:
            continue
        # left
        if col > 0 and int(inp[row][col - 1]) <= curVal:
            continue
        # right
        if col < colCount - 1 and int(inp[row][col + 1]) <= curVal:
            continue
        
        lowPoints.append((row, col))
        lowPointVals.append(curVal)

#print(sum(lowPointVals) + len(lowPointVals))

# find basins
basins = []
for lowPoint, lowPointVal in zip(lowPoints, lowPointVals):
    basin = set()
    basin.add((lowPoint, lowPointVal))

    newlyAdded = set()
    newlyAdded.add((lowPoint, lowPointVal))
    print('aaaaa')
    while len(newlyAdded) > 0:
        addedThisRound = set()
        for lowPoint, lowPointVal in newlyAdded:
            tryAdd = set()
            row, col = lowPoint
            curVal = lowPointVal
            if row > 0 and 9 > int(inp[row - 1][col]) and int(inp[row - 1][col]) > curVal:
                tryAdd.add(((row - 1, col), int(inp[row - 1][col])))
            # bottom
            if row < rowCount - 1 and 9 > int(inp[row + 1][col]) and int(inp[row + 1][col]) > curVal:
                tryAdd.add(((row + 1, col), int(inp[row + 1][col])))
            # left
            if col > 0 and 9 > int(inp[row][col - 1]) and int(inp[row][col - 1]) > curVal:
                tryAdd.add(((row, col - 1), int(inp[row][col - 1])))
            # right
            if col < colCount - 1 and 9 > int(inp[row][col + 1]) and int(inp[row][col + 1]) > curVal:
                tryAdd.add(((row, col + 1), int(inp[row][col + 1])))
            
            for x in tryAdd:
                if x not in basin:
                    print(x)
                    basin.add(x)
                    addedThisRound.add(x)
        newlyAdded = addedThisRound
    print('bbbbb')
    
    basins.append(basin)

print(basins)
print("Num basins: %s" % (len(basins)))
basins.sort(key=lambda basin: len(basin), reverse=True)
print(basins)
print([len(b) for b in basins])
print(len(basins[0]) * len(basins[1]) * len(basins[2]))
