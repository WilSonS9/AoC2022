with open('inp.txt', 'r') as f:
    jetStream = [*f.read()]

class Rock:
    def __init__(self, type, yMax):
        usedCoords = []
        if type == '-':
            usedCoords = [(x, yMax + 4) for x in range(2, 6)]
        elif type == '+':
            usedCoords = [(3, yMax + 6)] + [(x, yMax + 5) for x in range(2, 5)] + [(3, yMax + 4)]
        elif type == 'L':
            usedCoords = [(x, yMax + 4) for x in range(2, 5)] + [(4, yMax + 5), (4, yMax + 6)]
        elif type == 'I':
            usedCoords = [(2, y) for y in range(yMax + 4, yMax + 8)]
        elif type == 'O':
            usedCoords = [(x, y) for x in range(2, 4) for y in range(yMax + 4, yMax + 6)]
        self.usedCoords = usedCoords
    
    def simulateFall(self, totalUsedCoords, jetStream, i, yMax):
        while True:
            direction = jetStream[i % len(jetStream)]
            i += 1
            newCoords = self.push(direction)
            if self.isValid(newCoords):
                self.usedCoords = newCoords
            newCoords = self.push('v')
            if self.isValid(newCoords):
                self.usedCoords = newCoords
            else:
                totalUsedCoords += self.usedCoords
                yMax = max(yMax, max(self.usedCoords, key=lambda coord: coord[1])[1])
                break
        
        return totalUsedCoords, i, yMax

    def push(self, direction):
        newCoords = []
        if direction == '<':
            newCoords = list(map(lambda coord: (coord[0] - 1, coord[1]), self.usedCoords))
        elif direction == '>':
            newCoords = list(map(lambda coord: (coord[0] + 1, coord[1]), self.usedCoords))
        else:
            newCoords = list(map(lambda coord: (coord[0], coord[1] - 1), self.usedCoords))
        return newCoords

    def isValid(self, coords):
        return all(map(lambda coord: not coord in totalUsedCoords and coord[0] in range(7) and coord[1] > 0, coords))

def visualize(yMax):
    for y in range(yMax, 0, -1):
        row = '|'
        for x in range(7):
            if (x, y) in totalUsedCoords:
                row += '#'
            else:
                row += '.'
        row += '|'
        print(row)

i               = 0
yMax            = 0
types           = ['-', '+', 'L', 'I', 'O']
heightDiffs     = []
totalUsedCoords = []

for n in range(5000):
    type = types[n % len(types)]
    yMaxOld = yMax
    r = Rock(type, yMax)
    totalUsedCoords, i, yMax = r.simulateFall(totalUsedCoords, jetStream, i, yMax)
    heightDiffs.append(yMax - yMaxOld)
    if n % 100 == 0:
        print(n)

cycleSum    = 0
cycleOffset = 250
totalNRocks = 10**12

heightsToCheck = heightDiffs[cycleOffset:]

for cycleLength in range(5, len(heightDiffs)//2):
    hasCycled = heightsToCheck[:cycleLength] == heightsToCheck[cycleLength:2*cycleLength]
    if hasCycled:
        print('CYCLE DETECTED!')
        print(cycleLength)
        cycleSum = sum(heightsToCheck[:cycleLength])
        break

nCompleteCycles = (totalNRocks - cycleOffset) // cycleLength
remaining       = totalNRocks - cycleOffset - nCompleteCycles * cycleLength
print(nCompleteCycles, remaining)

s = sum(heightDiffs[:cycleOffset]) + nCompleteCycles * cycleSum + sum(heightsToCheck[:remaining])

print(s)