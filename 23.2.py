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
    elf['proposedMove'] = (row,col)

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

i = 0
while True:
    print(i)
    previousPositions = copy.deepcopy(currentPositions)
    proposedMoves = []
    for elf in elves:
        getProposal(elf)
    for elf in elves:
        move(elf)
    d = directions[0]
    directions.remove(d)
    directions.append(d)
    i += 1
    if currentPositions == previousPositions:
        print('REPEAT!!!!')
        break

print(i)