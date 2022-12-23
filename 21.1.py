with open('inp.txt', 'r') as f:
    l = list(map(lambda s: s.split(': '), f.read().split('\n')))

monkeys = {}
for line in l:
    key,val = line
    if val.isnumeric():
        monkeys[key] = int(val)
    else:
        x1, x2 = val.split(' ')[0], val.split(' ')[2]
        operation = eval(f'lambda {x1},{x2}, val=val: eval(val)')
        monkeys[key] = {'dependencies': (x1,x2), 'operation': operation}

def findValue(key, monkeys):
    if type(monkeys[key]) == int:
        return monkeys[key]
    else:
        operation = monkeys[key]['operation']
        dependencies = monkeys[key]['dependencies']
        return operation(findValue(dependencies[0], monkeys), findValue(dependencies[1], monkeys))

print(int(findValue('root', monkeys)))