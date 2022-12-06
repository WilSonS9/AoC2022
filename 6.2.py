with open('inp.txt', 'r') as f:
    l = f.read()

def isStart(chars):
    return len(set(chars)) == len(chars)

i = 0
while True:
    if isStart(l[i:i+14]):
        break
    i += 1

print(i+14)