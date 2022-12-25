from functools import reduce

with open('inp.txt', 'r') as f:
    l = map(lambda s: [*s], f.read().split('\n'))

values = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}

nDec = sum(map(lambda valueL: reduce(lambda a,b: 5 * int(a) + values[b], valueL), l))

def dec2snafu(n):
    if n:
        return dec2snafu((n + 2) // 5) + '=-012'[(n + 2) % 5]
    else:
        return ''

print(dec2snafu(nDec))