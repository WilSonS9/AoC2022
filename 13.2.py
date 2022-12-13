import ast
from functools import cmp_to_key

with open('inp.txt', 'r') as f:
    l = map(lambda s: s.split('\n'), f.read().split('\n\n'))

def compareElements(e1, e2):
    '1: in order, 0: not out of order, -1: out of order'
    if type(e1) == int and type(e2) == int:
        if e1 < e2:
            return 1
        elif e1 == e2:
            return 0
        else:
            return -1
    elif type(e1) == list and type(e2) == list:
        try:
            if compareElements(e1[0], e2[0]) == 1:
                return 1
            elif compareElements(e1[0], e2[0]) == 0:
                return compareElements(e1[1:], e2[1:])
            else:
                return -1
        except:
            if len(e1) == 0:
                if len(e2) > 0:
                    return 1
                else:
                    return 0
            else:
                return -1
    elif type(e1) == list:
        return compareElements(e1, [e2])
    else:
        return compareElements([e1], e2)

def compareLists(l1, l2):
    # print(f'    {l1}, {l2}')
    if len(l1) == 0 and len(l1) >= 0:
        return 1
    elif len(l1) > 0 and len(l2) == 0:
        return -1
    else:
        e1, e2 = l1[0], l2[0]
        elRes = compareElements(e1, e2)
        if elRes == 1:
            return 1
        elif elRes == 0:
            return compareLists(l1[1:], l2[1:])
        else:
            return -1

d1 = [[2]]
d2 = [[6]]
packets = [d1, d2]
for i, pair in enumerate(l):
    l1,l2 = map(lambda s: ast.literal_eval(s), pair)
    packets += [l1, l2]

packets.sort(key=cmp_to_key(compareLists), reverse=True)

print((packets.index(d1) + 1) * (packets.index(d2) + 1))