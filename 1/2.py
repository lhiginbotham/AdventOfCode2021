inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

first = True
prev = []
cur = 0
inc = 0
for x in inp:
    d = int(x)
    if len(prev) < 3:
        prev.append(d)
        continue
    if sum(prev[1:]) + d > sum(prev):
        inc += 1
    prev.append(d)
    if len(prev) > 3:
        prev.pop(0)

print(inc)