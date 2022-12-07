with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

fs = {}


class dir:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.children = []
        self.size = 0

    def addChild(self, isFile, value):
        'value: (name, size) for files, name for dirs'
        if isFile:
            self.children.append(value)
        else:
            self.children.append(value)

    def calculateSize(self):
        s = 0
        for child in self.children:
            if isinstance(child, tuple):
                s += child[1]
            else:
                s += fs[child].calculateSize()
        self.size = s
        return s

    def __repr__(self):
        return f'PARENT: {self.parent}, NAME: {self.name}, CHILDREN: {self.children}, SIZE: {self.size}'


cd = ''

for line in l:
    a = line.split(' ')
    if a[0] == '$':
        cmd = a[1]
        if cmd == 'cd':
            arg = a[2]
            if not arg == '..':
                if arg == '/':
                    cd = '/'
                else:
                    cd = f'{cd}{arg}/'
                if not cd in fs.keys():
                    fs[cd] = dir(cd, arg)
            else:
                cd = fs[cd].parent
        elif cmd == 'ls':
            pass
    else:
        if a[0] == 'dir':
            name = a[1]
            fs[f'{cd}{name}/'] = dir(cd, f'{cd}{name}/')
            fs[cd].addChild(False, f'{cd}{name}/')
        else:
            size, name = a
            size = int(size)
            fs[cd].addChild(True, (name,size))

usedTot = fs['/'].calculateSize()

totSpace = 70000000
minSpace = 30000000
freeSpace = totSpace - usedTot
freeSpaceDiff =  minSpace - freeSpace

dirs = list(fs.values())
dirs.sort(key=lambda val: val.size)
dirs = list(filter(lambda val: val.size >= freeSpaceDiff, dirs))

print(dirs[0].size)