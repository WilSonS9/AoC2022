with open('inp.txt', 'r') as f:
    coords = map(lambda s: tuple(map(int, s.split(','))), f.read().split('\n'))

cubes = {}

for coord in coords:
    x,y,z = coord
    sides = 6
    for neighbourCoord in [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]:
        if neighbourCoord in cubes.keys():
            cubes[neighbourCoord] -= 1
            sides -= 1
    
    cubes[coord] = sides

print(sum(cubes.values()))