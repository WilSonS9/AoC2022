with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

points = {'X': 1, 'Y': 2, 'Z': 3}

m1s = ['A', 'B', 'C']
m2s = ['X', 'Y', 'Z']

wins = [3, 0, 6]

def score(m1, m2):
    s = points[m2]
    idiff = (m1s.index(m1) - m2s.index(m2)) % 3
    s += wins[idiff]
    return s

l = list(map(lambda moves: moves.split(' '), l))

print(sum(list(map(lambda m: score(m[0], m[1]), l))))