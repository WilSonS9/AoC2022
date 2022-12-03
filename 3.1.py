with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

chars = [*'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']

s = 0
for sack in l:
    c1,c2 = set(sack[:int(len(sack)/2)]), set(sack[int(len(sack)/2):])
    common = list(c1.intersection(c2))[0]
    s += chars.index(common) + 1

print(s)