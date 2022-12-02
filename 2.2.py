with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

points = {'X': 1, 'Y': 2, 'Z': 3}

m1s = ['A', 'B', 'C']
m2s = ['X', 'Y', 'Z']

wins = [3, 0, 6]

def score(m1, end):
    s = 0
    if end == 'X':
        m2 = m2s[(m1s.index(m1) - 1) % 3]
    elif end == 'Y':
        m2 = m2s[m1s.index(m1)]
        s += 3
    else:
        m2 = m2s[(m1s.index(m1) - 2) % 3]
        s += 6
    s += points[m2]
    return s

l = list(map(lambda moves: moves.split(' '), l))

print(sum(list(map(lambda m: score(m[0], m[1]), l))))