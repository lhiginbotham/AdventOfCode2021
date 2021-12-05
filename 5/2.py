inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

maxX = 0
maxY = 0
grid = dict()

for line in inp:
    a = line.split(' -> ')
    startX, startY = a[0].split(',')
    startX = int(startX)
    startY = int(startY)
    endX, endY = a[1].split(',')
    endX = int(endX)
    endY = int(endY)

    maxX = max(startX, endX, maxX)
    maxY = max(startY, endY, maxY)

    smallerX = min(startX, endX)
    biggerX = max(startX, endX)
    smallerY = min(startY, endY)
    biggerY = max(startY, endY)

    print((startX, startY), (endX, endY), (smallerX, smallerY), (biggerX, biggerY))
    if startX == endX:
        for y in range(smallerY, biggerY + 1):
            if y not in grid:
                grid[y] = dict()
            if startX not in grid[y]:
                grid[y][startX] = 0
            grid[y][startX] = grid[y][startX] + 1
    elif startY == endY:
        for x in range(smallerX, biggerX + 1):
            #print(x)
            if startY not in grid:
                grid[startY] = dict()
            if x not in grid[startY]:
                grid[startY][x] = 0
            grid[startY][x] = grid[startY][x] + 1
    else:
        xInc = 1 if endX >= startX else -1
        yInc = 1 if endY >= startY else -1

        dist = abs(startX - endX)
        for z in range(dist + 1):
            x = startX + z * xInc
            y = startY + z * yInc
            if y not in grid:
                grid[y] = dict()
            if x not in grid[y]:
                grid[y][x] = 0
            grid[y][x] = grid[y][x] + 1
    #print(grid)

#print(maxX)
#print(maxY)
#print(grid)

numOverlap = 0
for r in range(maxY + 1):
    #print()
    for c in range(maxX + 1):
        if r not in grid:
            grid[r] = dict()
        if c not in grid[r]:
            grid[r][c] = 0
        #print(str(grid[r][c]) + ' ', end="")
        if grid[r][c] > 1:
            numOverlap += 1

#print()
print(numOverlap)