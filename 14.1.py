with open('inp.txt', 'r') as f:
    l = map(lambda s: s.split(' -> '), f.read().split('\n'))

usedTiles = set()

def sgn(x):
    if x >= 0:
        return 1
    else:
        return -1

for line in l:
    for i in range(len(line) - 1):
        sCoord, eCoord = line[i], line[i + 1]
        sx,sy = map(int, sCoord.split(','))
        ex,ey = map(int, eCoord.split(','))
        dx,dy = ex - sx, ey - sy
        if dx:
            coords = [(x, sy) for x in range(sx, ex + sgn(dx), sgn(dx))]
        else:
            coords = [(sx, y) for y in range(sy, ey + sgn(dy), sgn(dy))]
        for coord in coords:
            usedTiles.add(coord)

yMax = max(usedTiles, key=lambda coord: coord[1])[1]

def pourSand():
    x,y = 500, 0
    while True:
        if y > yMax:
            return 1
        if not (x, y+1) in usedTiles:
            y = y + 1
        elif not (x-1, y+1) in usedTiles:
            x, y = x-1, y+1
        elif not (x+1, y+1) in usedTiles:
            x, y = x+1, y+1
        else:
            # sand at rest
            usedTiles.add((x, y))
            break
    return 0

s = 0
while True:
    if not pourSand():
        s += 1
    else:
        break

print(s)