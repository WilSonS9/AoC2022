with open('inp.txt', 'r') as f:
    l = map(lambda s: s.split('\n'), f.read().split('\n\n'))

class Monkey:
    def __init__(self, items, op, divisor, mt, mf):
        self.items   = items
        self.op      = op
        self.divisor = divisor
        self.mt      = mt
        self.mf      = mf
        self.test    = lambda _: False
        self.nInsp   = 0
    
    def addItem(self, item):
        self.items.append(item)
    
    def inspect(self, monkeys):
        for worry in self.items:
            worry = tuple((self.op(remainder) % divisor for remainder, divisor in zip(worry, divisors)))
            if self.test(worry):
                monkeys[self.mt].addItem(worry)
            else:
                monkeys[self.mf].addItem(worry)
        self.nInsp += len(self.items)
        self.items = []

    def __repr__(self):
        return f'Items: {self.items} True: {self.mt} False: {self.mf} nInspect: {self.nInsp}'

divisors = []
monkeys = {}
for i, m in enumerate(l):
    items      = list(map(int, m[1].split(': ')[-1].split(', ')))
    divisor    = int(m[3].split(' ')[-1])
    op         = lambda old, m=m: eval(m[2].split('= ')[-1])
    mt         = int(m[4].split(' ')[-1])
    mf         = int(m[5].split(' ')[-1])
    divisors.append(int(m[3].split(' ')[-1]))
    monkeys[i] = Monkey(items, op, divisor, mt, mf)

for monkey in monkeys.values():
    monkey.items = [tuple((item % divisor for divisor in divisors)) for item in monkey.items]
    monkey.test  = lambda t, monkey=monkey: t[divisors.index(monkey.divisor)] % monkey.divisor == 0

for j in range(10000):
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        monkey.inspect(monkeys)
    if j % 100 == 0:
        print(j)

nInsps = [monkeys[i].nInsp for i in monkeys.keys()]
nInsps.sort(reverse=True)
print(nInsps[0] * nInsps[1])