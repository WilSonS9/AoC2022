import numpy as np

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

moves = list(map(lambda s: (s.split(' ')[0], int(s.split(' ')[1])), l))

xh, yh = 0, 0
xt, yt = xh, yh
positions = [(xt, yt)]

def sgn(x):
    if x >= 0:
        return 1
    else:
        return -1

def headCoords(xh, yh, d):
    if d == 'R':
        return xh + 1, yh
    elif d == 'L':
        return xh - 1, yh
    elif d == 'U':
        return xh, yh + 1
    else:
        return xh, yh - 1

def tailCoords(xh, yh, xt, yt):
    if (xt in [xh - 2, xh + 2] and yt == yh) or (yt in [yh - 2, yh + 2] and xt == xh):
        # not touching, sharing a row or column
        return (int(xt + 0.5 * (xh - xt)), int(yt + 0.5 * (yh - yt)))
    elif abs(xh - xt) + abs(yh - yt) >= 3:
        # not touching, not on same row or column
        return (xt + sgn(xh - xt), yt + sgn(yh - yt))
    else:
        return (xt, yt)

for move in moves:
    d, n = move
    for i in range(n):
        xh, yh = headCoords(xh, yh, d)
        xt, yt = tailCoords(xh, yh, xt, yt)
        if not (xt, yt) in positions:
            positions.append((xt, yt))

print(len(positions))