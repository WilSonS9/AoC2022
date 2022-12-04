with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

c = 0

for pair in l:
    s1,s2 = pair.split(',')
    l1,u1 = map(int, s1.split('-'))
    l2,u2 = map(int, s2.split('-'))
    c += (l1 <= l2 and u1 >= l2) or (l2 <= l1 and u2 >= l1)

print(c)