with open('inp.txt', 'r') as f:
    l = f.read().split('\n\n')

stackS, instructS = l

stacks = {}
instructs = []

lines = stackS.split('\n')
for i in range(1, len(lines[0]), 4):
    col = list(filter(lambda c: not c == ' ', [line[i] for line in lines]))
    colIndex = int(col[-1])
    stacks[colIndex] = col[:-1]

lines = instructS.split('\n')
for line in lines:
    line = line.replace('move ', '').replace(' from ', ',').replace(' to ', ',')
    n,fr,to = map(int, line.split(','))
    instructs.append((n,fr,to))

for instruct in instructs:
    n,fr,to = instruct
    stacks[to] = stacks[fr][:n][::-1] + stacks[to]
    stacks[fr] = stacks[fr][n:]

s = ''

for _,v in stacks.items():
    s += v[0]

print(s)