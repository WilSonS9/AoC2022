import numpy as np

with open('inp.txt', 'r') as f:
    rows = list(map(lambda s: list(map(int, [*s])), f.read().split('\n')))

A = np.array(rows)

scenicScores = []

for i in range(len(A[0])):
    for j in range(len(A)):
        el = A[i, j]

        down  = A[i+1:, j] < el
        up    = (A[:i, j]   < el)[::-1]
        right = A[i, j+1:] < el
        left  = (A[i, :j]   < el)[::-1]

        try:
            sd = [i for i, val in enumerate(down) if not val][0] + 1
        except:
            sd = len(A) - i - 1
        try:
            su = [i for i, val in enumerate(up) if not val][0] + 1
        except:
            su = i
        try:
            sr = [i for i, val in enumerate(right) if not val][0] + 1
        except:
            sr = len(A[0]) - j - 1
        try:
            sl = [i for i, val in enumerate(left) if not val][0] + 1
        except:
            sl = j

        score = sd*su*sr*sl
        scenicScores.append(score)

print(max(scenicScores))