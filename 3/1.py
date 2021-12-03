inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

c = 0
g = ""
e = ""

zer = dict()
one = dict()

maxDig = 0
for x in inp:
    i = 0
    for c in x:
        if c == '0':
            if i not in zer:
                zer[i] = 0
            zer[i] += 1
        else:
            if i not in one:
                one[i] = 0
            one[i] += 1
        i += 1
        if i > maxDig:
            maxDig = i

g = ""
e = ""
for x in range(maxDig):
    g = g + ("0" if zer[x] >= one[x] else "1")
    e = e + ("0" if zer[x] <= one[x] else "1")

print(g)
print(e)
print(int(g,2)*int(e,2))
#print(int(g, 2))
#print(int(e, 2))
#c = int(g,2) * int(e,2)
#print(c)