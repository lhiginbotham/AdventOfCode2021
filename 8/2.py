#
#
# I know this is a terrible, incoherent mess but I just wanted to be done, typing out my pathless logic :(
#
#
#

import collections

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

numOnes = 0
numFours = 0
numSevens = 0
numEights = 0

trueWireSetToNumber = {
    frozenset('abcefg'): "0",
    frozenset('cf'): "1",
    frozenset('acdeg'): "2",
    frozenset('acdfg'): "3",
    frozenset('bcdf'): "4",
    frozenset('abdfg'): "5",
    frozenset('abdefg'): "6",
    frozenset('acf'): "7",
    frozenset('abcdefg'): "8",
    frozenset('abcdfg'): "9",
}

solution = 0
for entry in inp:
    aliasWireToCandidateTrueWires = dict()

    digitWires, entryDisplay = entry.split(' | ')
    digitWireSplit = digitWires.split()

    aliasWireNumAppearances = collections.defaultdict(int)
    oneWires = None
    fourWires = None
    for digit in digitWireSplit:
        if len(digit) == 2:
            # this is a one, cf
            oneWires = digit
            #for d in digit:
                # aliasWireToCandidateTrueWires[d].add('c')
                # aliasWireToCandidateTrueWires[d].add('f')
        elif len(digit) == 4:
            # # this is a four, bcdf
            fourWires = digit
            # for d in digit:
                # #aliasWireToCandidateTrueWires[d].add('b')
                # aliasWireToCandidateTrueWires[d].add('c')
                # aliasWireToCandidateTrueWires[d].add('d')
                # aliasWireToCandidateTrueWires[d].add('f')
        # elif len(digit) == 3:
            # # this is a seven, acf
            # for d in digit:
                # aliasWireToCandidateTrueWires[d].add('a')
                # aliasWireToCandidateTrueWires[d].add('c')
                # aliasWireToCandidateTrueWires[d].add('f')
        # elif len(digit) == 7:
            # # this is an eight, abcdefg
            # for d in digit:
                # aliasWireToCandidateTrueWires[d].add('a')
                # #aliasWireToCandidateTrueWires[d].add('b')
                # aliasWireToCandidateTrueWires[d].add('c')
                # aliasWireToCandidateTrueWires[d].add('d')
                # #aliasWireToCandidateTrueWires[d].add('e')
                # #aliasWireToCandidateTrueWires[d].add('f')
                # aliasWireToCandidateTrueWires[d].add('g')

        for aliasWire in digit:
            aliasWireNumAppearances[aliasWire] += 1

    f = None
    dgCandidates = []
    for aliasWire in aliasWireNumAppearances:
        numAppearances = aliasWireNumAppearances[aliasWire]
        if numAppearances == 6:
            aliasWireToCandidateTrueWires[aliasWire] = set('b')
        elif numAppearances == 4:
            aliasWireToCandidateTrueWires[aliasWire] = set('e')
        elif numAppearances == 9:
            aliasWireToCandidateTrueWires[aliasWire] = set('f')
            f = aliasWire
        elif numAppearances == 7:
            aliasWireToCandidateTrueWires[aliasWire] = set('dg')
            dgCandidates.append(aliasWire)
        elif numAppearances == 8:
            #print(aliasWire + " is now a candidate for ac")
            aliasWireToCandidateTrueWires[aliasWire] = set('ac')

    # true f is paired with true c for digit 1, we can use this to solve this!
    cAlias = None
    if oneWires[0] == f:
        cAlias = oneWires[1]
    else:
        cAlias = oneWires[0]

    aliasWireToCandidateTrueWires[cAlias] = set('c')
    aAlias = [aliasWire for aliasWire in aliasWireToCandidateTrueWires if len(aliasWireToCandidateTrueWires[aliasWire]) == 2 and aliasWire != cAlias and 'a' in aliasWireToCandidateTrueWires[aliasWire]][0]
    aliasWireToCandidateTrueWires[aAlias] = set('a')
    #print("c alias = %s, a alias = %s" % (cAlias, aAlias))

    # now we only need to figure out 'd' and 'g' aliases.
    # luckily, d is used to represent four but g is not!
    if dgCandidates[0] in fourWires:
        aliasWireToCandidateTrueWires[dgCandidates[0]] = set('d')
        aliasWireToCandidateTrueWires[dgCandidates[1]] = set('g')
    else:
        aliasWireToCandidateTrueWires[dgCandidates[0]] = set('g')
        aliasWireToCandidateTrueWires[dgCandidates[1]] = set('d')

    # verify for my debugging sanity that this monstrosity worked...
    aliasToTrue = dict()
    for aliasWire in aliasWireToCandidateTrueWires:
        if len(aliasWireToCandidateTrueWires[aliasWire]) != 1:
            # print(aliasWireToCandidateTrueWires)
            # print(aliasWireToCandidateTrueWires[aliasWire])
            # print(aliasWire)
            print("This is wrong")
            exit()

        # clean up my stupid set maps
        aliasToTrue[aliasWire] = list(aliasWireToCandidateTrueWires[aliasWire])[0]


    # now start figuring out the message!!!
    trueDisplayNum = ""

    #print(entryDisplay)
    for displayNumberWires in entryDisplay.split():
        #print(displayNumberWires)
        # convert alias wire set to true wire set
        trueWireSet = set()
        for c in displayNumberWires:
            trueWireSet.add(aliasToTrue[c])

        #print(trueWireSet)

        # look up true wire set to see what the display should be
        trueDisplayNum += trueWireSetToNumber[frozenset(trueWireSet)]

    # convert to number and add it to the solution...
    print(trueDisplayNum)
    solution += int(trueDisplayNum)

print(solution)
