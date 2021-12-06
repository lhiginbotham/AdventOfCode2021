inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

fishMap = dict()
for x in range(9):
    fishMap[x] = 0

for x in inp[0].split(','):
    ix = int(x)
    if ix not in fishMap:
        fishMap[ix] = 0
    fishMap[ix] += 1

print('ab')
print(len(fishMap))
print(fishMap)
print(sum([fishMap[x] for x in fishMap.keys()]))

for day in range(256):
    newFishMap = dict()
    for idx in range(9):
        newFishMap[idx] = 0

    for idx in range(9):
        currCount = fishMap[idx]
        
        ageGroup = idx - 1
        if ageGroup < 0:
            ageGroup = 6
            newFishMap[8] += currCount

        newFishMap[ageGroup] += currCount

    fishMap = newFishMap
    print("day: " + str(day + 1))
    print(sum([fishMap[x] for x in fishMap.keys()]))

