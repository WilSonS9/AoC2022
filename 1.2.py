with open('inp.txt', 'r') as f:
    l = map(lambda f: f.split('\n'), f.read().split('\n\n'))

l = list(map(lambda elf: sum(map(int, elf)), l))
l.sort(reverse=True)

print(sum(l[:3]))