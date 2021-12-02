inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

hp = 0
dp = 0
aim = 0
for x in inp:
    a = x.split()
    direction = a[0]
    dist = int(a[1])
    if direction == "forward":
        hp += dist
        dp += aim * dist
    elif direction == "down":
        aim += dist
    elif direction == "up":
        aim -= dist

print(hp)
print(dp)
print(hp*dp)