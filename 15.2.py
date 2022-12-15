with open('inp.txt', 'r') as f:
    l = map(lambda s: s.split('='), f.read().split('\n'))

sensors = []

def isCovered(x, y):
    for sensor in sensors:
        sx, sy, dist = sensor
        if abs(sx - x) + abs(sy - y) <= dist:
            return 1
    return 0

def points(sx, sy, dist):
    'points one unit outside the edge of a sensor'
    l = []
    for d in range(dist + 2):
        dx = d
        dy = dist - d + 1
        l += [(sx + dx, sy + dy), (sx + dx, sy - dy), (sx - dx, sy + dy), (sx - dx, sy - dy)]
    return l

for s in l:
    sx = int(s[1].split(',')[0])
    sy = int(s[2].split(':')[0])
    bx = int(s[3].split(',')[0])
    by = int(s[4])
    dist = abs(sx - bx) + abs(sy - by)
    sensors.append((sx, sy, dist))

def getAnswer():
    for sensor in sensors:
        sx, sy, dist = sensor
        for point in points(sx, sy, dist):
            x, y = point
            if x in range(4000000 + 1) and y in range(4000000 + 1) and not isCovered(x, y):
                return 4000000 * x + y

print(getAnswer())