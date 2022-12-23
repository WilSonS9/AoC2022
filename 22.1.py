with open('inp.txt', 'r') as f:
    worldS,instructS = f.read().split('\n\n')

world = []
chars = {}

for row,line in enumerate(worldS.split('\n')):
    rowL = []
    for col,char in enumerate(line):
        rowL.append((row,col))
        if not char == ' ':
            chars[(row,col)] = char
    world.append(rowL)

instructs = []
rotations = {'R': 0 - 1j, 'L': 0 + 1j}
dirValues = [(0, 1), (1, 0), (0, -1), (-1, 0)]

i = 0
while i < len(instructS):
    if instructS[i].isdigit() and i + 1 <= len(instructS) - 1 and instructS[i+1].isdigit():
        instructs.append(int(''.join(instructS[i:i+2])))
        i += 1
    elif instructS[i].isdigit():
        instructs.append(int(instructS[i]))
    else:
        instructs.append(rotations[instructS[i]])
    i += 1

def rotateDirection(currentDir, rotation):
    dx, dy = currentDir
    newDirC = (dx + dy * 1j) * rotation
    return (int(newDirC.real), int(newDirC.imag))

def move(coord, currentDir):
    row,col = coord
    dy,dx   = currentDir

    row += dy
    col += dx
    if (row, col) in chars.keys():
        if chars[(row, col)] == '.':
            return (row, col)
        else:
            return coord
    else:
        if dx == 0:
            column = [rowL[col] for rowL in world if col <= rowL[-1][1] and rowL[col][1] == col and rowL[col] in chars.keys()]
            if row < column[0][0]:
                row = column[-1][0]
            else:
                row = column[0][0]
        else:
            rowL = list(filter(lambda coord: coord in chars.keys(), world[row]))
            if col < rowL[0][1]:
                col = rowL[-1][1]
            else:
                col = rowL[0][1]
        if chars[(row,col)] == '.':
            return (row, col)
        else:
            return coord

def executeInstruct(instruct, currentCoord, currentDir):
    if type(instruct) == complex:
        rotation   = instruct
        currentDir = rotateDirection(currentDir, rotation)
    else:
        length     = instruct
        for _ in range(length):
            currentCoordOld = currentCoord
            currentCoord    = move(currentCoord, currentDir)
            if currentCoord == currentCoordOld:
                break
    return currentCoord, currentDir

def calculateScore(currentCoord, currentDir):
    row,col = currentCoord
    return 1000 * (row + 1) + 4 * (col + 1) + dirValues.index(currentDir)


# manually check input for which column
currentCoord = world[0][0]
currentDir   = (0, 1)

for instruct in instructs:
    currentCoord, currentDir = executeInstruct(instruct, currentCoord, currentDir)

print(calculateScore(currentCoord, currentDir))