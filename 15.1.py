with open('inp.txt', 'r') as f:
    l = map(lambda s: s.split('='), f.read().split('\n'))

sensorCoords = []
beaconCoords = []
usedCoords = set()
yTarget = 2000000
                
for s in l:
    sx = int(s[1].split(',')[0])
    sy = int(s[2].split(':')[0])
    bx = int(s[3].split(',')[0])
    by = int(s[4])
    dist = abs(sx - bx) + abs(sy - by)
    sensorCoords.append((sx, sy))
    beaconCoords.append((bx, by))
    for dx in range(dist - abs(sy - yTarget) + 1):
        usedCoords.add((sx + dx, yTarget))
        usedCoords.add((sx - dx, yTarget))

print(len(list(filter(lambda coord: coord not in beaconCoords, usedCoords))))