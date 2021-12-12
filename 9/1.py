inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

rowCount = len(inp)
colCount = len(inp[0])

#def findLowPoints(inp):
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

print(sum(lowPointVals) + len(lowPointVals))
