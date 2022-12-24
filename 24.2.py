from functools import reduce

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

blizzards      = []
openPositions  = set()
blizzardCoords = set()

directions = {'<': (0, -1), 'v': (1, 0), '>': (0, 1), '^': (-1, 0)}

for row, line in enumerate(l):
    for col, c in enumerate(line):
        if c == '.':
            openPositions.add((row - 1,col - 1))
        elif c in '<v>^':
            blizzards.append((row - 1,col - 1, c))
            blizzardCoords.add((row - 1, col - 1))

maxRow = len(l) - 2
minRow = -1
maxCol = len(l[0]) - 2
minCol = -1

start = (-1, 0)
end   = (maxRow, maxCol - 1)

def moveBlizzard(coord, direction):
    row,col   = coord
    dRow,dCol = directions[direction]
    nRow,nCol = (row + dRow) % maxRow, (col + dCol) % maxCol
    return (nRow, nCol)

def simulateBlizzards():
    newBlizzards = []
    for blizzard in blizzards:
        row,col,direction = blizzard
        nRow,nCol = moveBlizzard((row,col), direction)
        newBlizzards.append((nRow,nCol,direction))
    blizzardCoords = set({(row,col) for row,col,direction in newBlizzards})
    newPositions  = set({start, end})
    for row in range(maxRow):
        for col in range(maxCol):
            if not (row,col) in blizzardCoords:
                newPositions.add((row,col))
    return newBlizzards, newPositions

def generateFutureStates(currentPos):
    row,col         = currentPos
    futurePositions = []
    for futurePos in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1), (row, col)]:
        if futurePos in openPositions:
            futurePositions.append(futurePos)
    return futurePositions

currentPositions = set({start})
i = 0
while True:
    blizzards, openPositions = simulateBlizzards()
    currentPositions = set(reduce(lambda a,b: a + b, [generateFutureStates(position) for position in currentPositions]))
    print(i, len(currentPositions))
    i += 1
    if end in currentPositions:
        print('FOUND PATH TO END!!!!')
        print(i)
        break

currentPositions = set({end})
while True:
    blizzards, openPositions = simulateBlizzards()
    currentPositions = set(reduce(lambda a,b: a + b, [generateFutureStates(position) for position in currentPositions]))
    print(i, len(currentPositions))
    i += 1
    if start in currentPositions:
        print('FOUND PATH TO BEGINNING!!!!')
        print(i)
        break

currentPositions = set({start})
while True:
    blizzards, openPositions = simulateBlizzards()
    currentPositions = set(reduce(lambda a,b: a + b, [generateFutureStates(position) for position in currentPositions]))
    print(i, len(currentPositions))
    i += 1
    if end in currentPositions:
        print('FOUND PATH TO END!!!!')
        print(i)
        break