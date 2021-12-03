inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

c = 0
g = ""
e = ""

zer = None
one = None

maxDig = 0

def genDictionaries(inputArr):
    global maxDig, zer, one
    zer = dict()
    one = dict()

    for x in inputArr:
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

genDictionaries(inp)
g = ""
e = ""
for x in range(maxDig):
    g = g + ("0" if zer[x] >= one[x] else "1")
    e = e + ("0" if zer[x] <= one[x] else "1")

print(g)
print(e)
#print(int(g,2)*int(e,2))
#print(int(g, 2))
#print(int(e, 2))
#c = int(g,2) * int(e,2)
#print(c)

# pt 2

inp2 = inp[:]
print(zer)
print(one)
while len(inp) > 1:
    for x in range(maxDig):
        #print(inp)
        if zer[x] > one[x]:
            inp = [a for a in inp if a[x] == "0"]
        else:
            inp = [a for a in inp if a[x] == "1"]

        if len(inp) <= 1:
            break

        genDictionaries(inp)

    print(zer)
    print(one)

genDictionaries(inp2)
while len(inp2) > 1:
    for x in range(maxDig):
        if zer[x] <= one[x]:
            inp2 = [a for a in inp2 if a[x] == "0"]
        else:
            inp2 = [a for a in inp2 if a[x] == "1"]

        if len(inp2) <= 1:
            break

        genDictionaries(inp2)

print(inp)
#print(inp2)
print(int(inp[0], 2) * int(inp2[0], 2))