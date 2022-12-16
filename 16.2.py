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
    'currentNodeP': 'AA',
    'currentNodeE': 'AA',
    'totalFlow': 0,
    'openedValves': []
}

states = [currentState]

def generateFutureStates(state, timeLeft):
    'Generates all possible future states 1 minute in the future'
    currentNodeP, currentNodeE, totalFlow, openedValves = state.values()
    flowRateP = nodes[currentNodeP]['flowRate']
    flowRateE = nodes[currentNodeE]['flowRate']

    newStates = []
    pairs = []
    for neighbourP in nodes[currentNodeP]['neighbours']:
        for neighbourE in nodes[currentNodeE]['neighbours']:
            pair = [neighbourP, neighbourE]
            if not pair in pairs:
                # both move
                pairs.append(sorted(pair))
                newStates.append({
                    'currentNodeP': neighbourP,
                    'currentNodeE': neighbourE,
                    'totalFlow': totalFlow,
                    'openedValves': openedValves
                })
        if not currentNodeE in openedValves and flowRateE > 0:
            # person moves, elephant opens valve
            newStates.append({
                'currentNodeP': neighbourP,
                'currentNodeE': currentNodeE,
                'totalFlow': totalFlow + flowRateE * (timeLeft - 1),
                'openedValves': openedValves + [currentNodeE]
            })
    
    if not currentNodeP in openedValves and flowRateP > 0:
        # person opens valve, elephant moves
        for neighbourE in nodes[currentNodeE]['neighbours']:
            newStates.append({
                'currentNodeP': currentNodeP,
                'currentNodeE': neighbourE,
                'totalFlow': totalFlow + flowRateP * (timeLeft - 1),
                'openedValves': openedValves + [currentNodeP]
            })
        if not currentNodeE in openedValves and flowRateE > 0 and not currentNodeE == currentNodeP:
            # both open valves
            newStates.append({
                'currentNodeP': currentNodeP,
                'currentNodeE': currentNodeE,
                'totalFlow': totalFlow + flowRateE * (timeLeft - 1) + flowRateP * (timeLeft - 1),
                'openedValves': openedValves + [currentNodeE] + [currentNodeP]
            })

    return newStates

# print(generateFutureStates(currentState, 26))

for timeLeft in range(26, 0, -1):
    if timeLeft % 2 == 0:
        # only save the 3000 best states every 5 minutes
        states.sort(key=lambda state: state['totalFlow'], reverse=True)
        states = states[:2000]
    states = list(reduce(lambda a,b: a + b, [generateFutureStates(state, timeLeft) for state in states]))
    print(timeLeft, len(states))

states.sort(key=lambda state: state['totalFlow'], reverse=True)
print(states[0])