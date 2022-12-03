with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

sacks = [l[i:i+3] for i in range(0, len(l) - 2, 3)]

chars = [*'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']

s = 0
for sack3s in sacks:
    s1,s2,s3 = set(sack3s[0]), set(sack3s[1]), set(sack3s[2])
    common = list(s1.intersection(s2).intersection(s3))[0]
    s += chars.index(common) + 1

print(s)