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

s = 0
for cycleN in range(19, 220, 40):
    strength = (cycleN + 1) * Xs[cycleN]
    s += strength

print(s)