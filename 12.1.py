import string
import networkx as nx

with open('inp.txt', 'r') as f:
    l = list(map(lambda s: [*s], f.read().split('\n')))

def getNeighbours(i, j, l):
    outp = []
    for coord in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if coord[0] in range(0, len(l)) and coord[1] in range(0, len(l[0])):
            outp.append(coord)
    return outp

def shortestPath(S, E):
    pathLength = nx.shortest_path_length(G, source=S, target=E)
    return pathLength

alpha = {string.ascii_lowercase[i]: i for i in range(len(string.ascii_lowercase))}
alpha.update({'S': 0, 'E': 25})
G = nx.DiGraph()

for i,r in enumerate(l):
    for j,c in enumerate(r):
        neighbours = getNeighbours(i, j, l)
        for coord in neighbours:
            n = l[coord[0]][coord[1]]
            if alpha[n] <= alpha[c] + 1:
                G.add_edge((i, j), coord)

# manual lookup
S = (20, 0)
E = (20, 91)

pathLength = shortestPath(S, E)
print(pathLength)