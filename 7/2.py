inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

minP = None
maxP = None
crabs = []
crabRanges = []

for x in inp[0].split(','):
    crabs.append(int(x))
    if minP == None:
        minP = int(x)
    if maxP == None:
        maxP = int(x)
    minP = min(minP, int(x))
    maxP = max(maxP, int(x))

posBest = -1
bestFuelConsumption = None
for x in range(minP, maxP + 1):
    fuelConsumption = 0
    for crab in crabs:
        dist = abs(x - crab)
        crabFuelNeeded = 0
        fuelCost = 1
        # for i in range(dist):
            # crabFuelNeeded += fuelCost
            # fuelCost += 1
        fuelConsumption += (dist * (dist + 1))/2
    if bestFuelConsumption is None or fuelConsumption < bestFuelConsumption:
        posBest = x
        bestFuelConsumption = fuelConsumption

print(bestFuelConsumption)
