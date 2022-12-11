with open('inp.txt', 'r') as f:
    l = map(lambda s: s.split('\n'), f.read().split('\n\n'))

class Monkey:
    def __init__(self, items, op, test, mt, mf):
        self.items = items
        self.op    = op
        self.test  = test
        self.mt    = mt
        self.mf    = mf
        self.nInsp = 0
    
    def addItem(self, item):
        self.items.append(item)
    
    def inspect(self, monkeys):
        for worry in self.items:
            worry = self.op(worry)
            worry //= 3
            if self.test(worry):
                monkeys[self.mt].addItem(worry)
            else:
                monkeys[self.mf].addItem(worry)
        self.nInsp += len(self.items)
        self.items = []

    def __repr__(self):
        return f'Items: {self.items} True: {self.mt} False: {self.mf} nInspect: {self.nInsp}'

monkeys = {}
for i, m in enumerate(l):
    items      = list(map(int, m[1].split(': ')[-1].split(', ')))
    op         = lambda old, m=m: eval(m[2].split('= ')[-1])
    test       = lambda w, m=m: w % int(m[3].split(' ')[-1]) == 0
    mt         = int(m[4].split(' ')[-1])
    mf         = int(m[5].split(' ')[-1])
    monkeys[i] = Monkey(items, op, test, mt, mf)

for i in range(20):
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        monkey.inspect(monkeys)

nInsps = [monkeys[i].nInsp for i in monkeys.keys()]
nInsps.sort(reverse=True)
print(nInsps[0] * nInsps[1])