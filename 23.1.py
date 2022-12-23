import copy

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

elves = []
currentPositions = set()
for row,line in enumerate(l):
    for col,c in enumerate(line):
        if c == '#':
            elves.append({
                'currentPos': (row, col),
                'proposedMove': ()
            })
            currentPositions.add((row, col))

directions    = ['N', 'S', 'W', 'E']
proposedMoves = []

def getProposal(elf):
    row, col = elf['currentPos']
    if (not (row - 1, col - 1) in currentPositions and not (row - 1, col) in currentPositions and not (row - 1, col + 1) in currentPositions
        and not (row, col - 1) in currentPositions and not (row, col + 1) in currentPositions
        and not (row + 1, col - 1) in currentPositions and not (row + 1, col) in currentPositions and not (row + 1, col + 1) in currentPositions):
        elf['proposedMove'] = (row, col)
    else:
        for d in directions:
            if d == 'N':
                if not (row - 1, col - 1) in currentPositions and not (row - 1, col) in currentPositions and not (row - 1, col + 1) in currentPositions:
                    elf['proposedMove'] = (row - 1, col)
                    break
            elif d == 'S':
                if not (row + 1, col - 1) in currentPositions and not (row + 1, col) in currentPositions and not (row + 1, col + 1) in currentPositions:
                    elf['proposedMove'] = (row + 1, col)
                    break
            elif d == 'W':
                if not (row + 1, col - 1) in currentPositions and not (row, col - 1) in currentPositions and not (row - 1, col - 1) in currentPositions:
                    elf['proposedMove'] = (row, col - 1)
                    break
            elif d == 'E':
                if not (row + 1, col + 1) in currentPositions and not (row, col + 1) in currentPositions and not (row - 1, col + 1) in currentPositions:
                    elf['proposedMove'] = (row, col + 1)
                    break
    proposedMoves.append(elf['proposedMove'])

def move(elf):
    if proposedMoves.count(elf['proposedMove']) == 1:
        currentPositions.remove(elf['currentPos'])
        currentPositions.add(elf['proposedMove'])
        elf['currentPos'] = elf['proposedMove']

def calculateScore():
    minRow = min(coord[0] for coord in currentPositions)
    maxRow = max(coord[0] for coord in currentPositions)
    minCol = min(coord[1] for coord in currentPositions)
    maxCol = max(coord[1] for coord in currentPositions)

    # no idea why but this works???
    return (maxRow - minRow + 2) * (maxCol - minCol + 2) - len(currentPositions)

def visualize(minRow, maxRow, minCol, maxCol):
    for row in range(minRow, maxRow + 1):
        r = ''
        for col in range(minCol, maxCol + 1):
            coord = (row,col)
            if coord in currentPositions:
                r += '#'
            else:
                r += '.'
        print(r)

for i in range(10):
    print(i)
    previousElves = copy.deepcopy(elves)
    # print(elves)
    # print([elf['currentPos'] for elf in elves])
    # print(directions)
    # print(30 * '-')
    proposedMoves = []
    for elf in elves:
        getProposal(elf)
    for elf in elves:
        move(elf)
    d = directions[0]
    directions.remove(d)
    directions.append(d)
    print(directions)
    if elves == previousElves:
        print('REPEAT!!!!')
        break

print(10)
minRow = min([elf['currentPos'][0] for elf in elves])
maxRow = max([elf['currentPos'][0] for elf in elves])
minCol = min([elf['currentPos'][1] for elf in elves])
maxCol = max([elf['currentPos'][1] for elf in elves])
visualize(minRow - 3, maxRow + 3, minCol - 3, maxCol + 3)
    
print(calculateScore())