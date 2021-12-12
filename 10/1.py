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

syntaxScore = 0
for line in inp:
    chunkStack = []
    for c in line:
        if c in ')}]>':
            if len(chunkStack) < 1:
                syntaxScore += score(c)
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
                break
            chunkStack.pop()
        else:
            chunkStack.append(c)

print(syntaxScore)
