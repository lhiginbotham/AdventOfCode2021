import copy

inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

callingNumbers = [int(num) for num in inp[0].split(',')]

boards = []

board = []
for x in inp[2:]:
    if len(x) < 1:
        continue
    else:
        row = [int(num) for num in x.split()]
        board.append(row)
        if len(board) == 5:
            boards.append(board)
            board = []

def callNewNumber(boards, calledNumber):
    for board in boards:
        for row in range(5):
            for col in range(5):
                if board[row][col] == calledNumber:
                    board[row][col] = -1 # marked sentinel

def checkForWinner(boards):
    index = -1
    for board in boards:
        index += 1
        # check for horizontal wins
        for row in range(5):
            winner = True
            for col in range(5):
                if board[row][col] != -1:
                    winner = False
                    break
            if winner:
                return index
        
        # check for vertical wins
        for col in range(5):
            winner = True
            for row in range(5):
                if board[row][col] != -1:
                    winner = False
                    break
            if winner:
                return index

    return -1

def calculateWinnerPoints(boards, winnerIndex, winningNumber):
    if winnerIndex < 0 or winnerIndex >= len(boards):
        return 0

    winner = boards[winnerIndex]
    unmarkedSum = 0
    for row in winner:
        for val in row:
            if val != -1:
                unmarkedSum += val

    return unmarkedSum * winningNumber

def runGame(boards, callingNumbers):
    markedBoards = copy.deepcopy(boards)
    winnerIndex = -1
    winningNumber = -1

    for x in callingNumbers:
        callNewNumber(markedBoards, x)
        winnerIndex = checkForWinner(markedBoards)
        if winnerIndex > -1:
            print("Winning number %s, winning index %s" % (x, winnerIndex))
            winningNumber = x
            break

    return calculateWinnerPoints(markedBoards, winnerIndex, winningNumber)

winningScore = runGame(boards, callingNumbers)
print(winningScore)

