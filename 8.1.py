import numpy as np

with open('inp.txt', 'r') as f:
    rows = list(map(lambda s: list(map(int, [*s])), f.read().split('\n')))

A = np.array(rows)

s = 0

for i in range(len(A[0])):
    for j in range(len(A)):
        el = A[i, j]
        if np.all(A[i+1:, j] < el) or np.all(A[:i, j] < el) or np.all(A[i, j+1:] < el) or np.all(A[i, :j] < el):
            s += 1

print(s)