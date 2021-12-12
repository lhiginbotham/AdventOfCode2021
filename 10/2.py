inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

def score(end):
    if end == ')':
        return 3
    elif end == ']':
        return 57
    elif end == '}':
        return 1197
    elif end == '>':
        return 25137
    return 0

def scoreAuto(end):
    if end == ')':
        return 1
    elif end == ']':
        return 2
    elif end == '}':
        return 3
    elif end == '>':
        return 4
    return 0

def closePair(start):
    if start == '(':
        return ')'
    elif start == '[':
        return ']'
    elif start == '{':
        return '}'
    elif start == '<':
        return '>'
    return ''

syntaxScore = 0
autocompleteScores = []
for line in inp:
    chunkStack = []
    corrupt = False
    for c in line:
        if c in ')}]>':
            if len(chunkStack) < 1:
                syntaxScore += score(c)
                corrupt = True
                break
            parentheses = '()'
            braces = '{}'
            brackets = '[]'
            angleBrackets = '<>'
            left = chunkStack[-1]
            pair = ''
            if left in parentheses:
                pair = parentheses
            elif left in braces:
                pair = braces
            elif left in brackets:
                pair = brackets
            elif left in angleBrackets:
                pair = angleBrackets
            if c not in pair:
                syntaxScore += score(c)
                corrupt = True
                break
            chunkStack.pop()
        else:
            chunkStack.append(c)

    if corrupt:
        continue

    autocompleteScore = 0
    while len(chunkStack) > 0:
        autocompleteScore *= 5
        autocompleteScore += scoreAuto(closePair(chunkStack.pop()))

    autocompleteScores.append(autocompleteScore)

autocompleteScores.sort()
print(autocompleteScores[int(len(autocompleteScores) / 2)])

