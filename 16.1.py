from functools import reduce

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

nodes = {}
for line in l:
    valve = line.split('Valve ')[1].split(' ')[0]
    flowRate = int(line.split(';')[0].split('=')[-1])
    neighbours = ''.join(line.split('valve')[1].split(' ')[1:]).split(',')
    nodes[valve] = {'flowRate': flowRate, 'neighbours': neighbours}

currentState = {
    'currentNode': 'AA',
    'totalFlow': 0,
    'openedValves': []
}

states = [currentState]

def generateFutureStates(state, timeLeft):
    'Generates all possible future states 1 minute in the future'
    currentNode, totalFlow, openedValves = state.values()
    flowRate = nodes[currentNode]['flowRate']
    newStates = []
    for neighbour in nodes[currentNode]['neighbours']:
        # move to a neighbour
        newStates.append({
            'currentNode': neighbour,
            'totalFlow': totalFlow,
            'openedValves': openedValves
        })
    if not currentNode in openedValves and flowRate > 0:
        # open the valve
        newStates.append({
            'currentNode': currentNode,
            'totalFlow': totalFlow + flowRate * (timeLeft - 1),
            'openedValves': openedValves + [currentNode]
        })

    return newStates

for timeLeft in range(30, 0, -1):
    if timeLeft % 3 == 0:
        # only save the 3000 best states every 5 minutes
        states.sort(key=lambda state: state['totalFlow'], reverse=True)
        states = states[:3000]
    states = list(reduce(lambda a,b: a + b, [generateFutureStates(state, timeLeft) for state in states]))
    print(timeLeft, len(states))

states.sort(key=lambda state: state['totalFlow'], reverse=True)
print(states[0])