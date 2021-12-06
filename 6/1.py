inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

fish = []

class Fish():
    def __init__(self, timer):
        self.timer = timer

    def age(self):
        self.timer -= 1
        if self.timer < 0:
            fish.append(Fish(8))
            self.timer = 6

for x in inp[0].split(','):
    fish.append(Fish(int(x)))

print(len(fish))

for day in range(80):
    for fishIdx in range(len(fish)):
        f = fish[fishIdx]
        f.age()
    print("day: " + str(day + 1))
    print(len(fish))

