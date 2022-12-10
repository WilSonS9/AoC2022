with open('inp.txt', 'r') as f:
    l = map(lambda s: s.split(' '), f.read().split('\n'))

instructs = []
for s in l:
    if len(s) == 1:
        instructs.append(s[0])
    else:
        instructs.append((s[0], int(s[1])))

X  = 1
Xs = []

for instruct in instructs:
    Xs.append(X)
    if len(instruct) == 2:
        # addx
        val = instruct[1]

        # wait one cycle where X doesn't change
        Xs.append(X)
        X += val

for i in range(6):
    row = ''
    for j in range(40):
        cycleN = i * 40 + j + 1
        X = Xs[cycleN - 1]
        if X in range(j - 1, j + 2):
            row += '#'
        else:
            row += '.'
    print(row)