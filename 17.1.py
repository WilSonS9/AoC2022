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
    
    def simulateFall(self, totalUsedCoords, jetStream, i):
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
                break
        
        return totalUsedCoords, i

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
            
i               = 0
yMax            = 0
types           = ['-', '+', 'L', 'I', 'O']
totalUsedCoords = []

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

for n in range(2022):
    print(n)
    type = types[n % len(types)]
    r = Rock(type, yMax)
    totalUsedCoords, i = r.simulateFall(totalUsedCoords, jetStream, i)
    yMax = max(totalUsedCoords, key=lambda coord: coord[1])[1]

print(yMax)