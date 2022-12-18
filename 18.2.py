with open('inp.txt', 'r') as f:
    coords = map(lambda s: tuple(map(int, s.split(','))), f.read().split('\n'))

cubes = {}

def adjacentCubes(x, y, z):
    return [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]

for coord in coords:
    x,y,z = coord
    sides = 6
    for neighbourCoord in adjacentCubes(x, y, z):
        if neighbourCoord in cubes.keys():
            cubes[neighbourCoord] -= 1
            sides -= 1
    cubes[coord] = sides

xs, ys, zs = zip(*cubes.keys())

scannedCubes = set(cubes.keys())
universe     = set((x, y, z) for x in range(min(xs) - 1, max(xs) + 2) for y in range(min(ys) - 1, max(ys) + 2) for z in range(min(zs) - 1, max(zs) + 2))
emptyCubes   = universe - scannedCubes

q = [(min(xs) - 1, min(ys) - 1, min(zs) - 1)]
while q:
    coord, q = q[0], q[1:]
    if coord in emptyCubes:
        emptyCubes.remove(coord)
        x,y,z = coord
        q += adjacentCubes(x,y,z)

for cube in emptyCubes:
    x,y,z = cube
    sides = 6
    for neighbourCoord in adjacentCubes(x, y, z):
        if neighbourCoord in cubes.keys():
            cubes[neighbourCoord] -= 1
            sides -= 1

print(sum(cubes.values()))