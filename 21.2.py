with open('inp.txt', 'r') as f:
    l = list(map(lambda s: s.split(': '), f.read().split('\n')))

monkeys = {}
for line in l:
    key,val = line
    if val.isnumeric():
        monkeys[key] = val
    elif key == 'root':
        x1, op, x2 = val.split(' ')
        op = '='
        monkeys[key] = {'dependencies': (x1,x2), 'operation': op}
    else:
        x1, op, x2 = val.split(' ')
        monkeys[key] = {'dependencies': (x1,x2), 'operation': op}

monkeys['humn'] = 'x'

def buildEquation(key, monkeys):
    if type(monkeys[key]) == str:
        return monkeys[key]
    else:
        op = monkeys[key]['operation']
        dependencies = monkeys[key]['dependencies']
        x1, x2 = buildEquation(dependencies[0], monkeys), buildEquation(dependencies[1], monkeys)
        return f'({x1} {op} {x2})'

print(buildEquation('root', monkeys))