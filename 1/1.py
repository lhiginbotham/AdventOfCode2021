inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

first = True
prev = 0
inc = 0
for x in inp:
    d = int(x)
    if first:
        first = False
        prev = d
        continue
    if d > prev:
        inc += 1
    prev = d

print(inc)