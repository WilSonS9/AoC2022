from functools import reduce

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

blueprints = {}

for i,bprint in enumerate(l):
    rs = list(map(lambda s: s.split(' '), bprint.split('. ')))

    ore      = {'oreCost': int(rs[0][-2])}
    clay     = {'oreCost': int(rs[1][-2])}
    obsidian = {'oreCost': int(rs[2][4]), 'clayCost': int(rs[2][7])}
    geode    = {'oreCost': int(rs[3][4]), 'obsidianCost': int(rs[3][7])}

    blueprints[i+1] = {'oreRobot': ore, 'clayRobot': clay, 'obsidianRobot': obsidian, 'geodeRobot': geode}

startState = {'nOreRobots': 1, 'nClayRobots': 0, 'nObsidianRobots': 0, 'nGeodeRobots': 0, 'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}

def generateFutureStates(state, blueprint):
    'Generates all possible future states 1 minute in the future'
    nOreRobots, nClayRobots, nObsidianRobots, nGeodeRobots, ore, clay, obsidian, geode = state.values()

    newStates = []

    newStates.append({'nOreRobots': nOreRobots, 'nClayRobots': nClayRobots, 'nObsidianRobots': nObsidianRobots, 'nGeodeRobots': nGeodeRobots,
                        'ore': ore + nOreRobots, 'clay': clay + nClayRobots,
                        'obsidian': obsidian + nObsidianRobots, 'geode': geode + nGeodeRobots})

    if ore >= blueprint['oreRobot']['oreCost']:
        newStates.append({'nOreRobots': nOreRobots + 1, 'nClayRobots': nClayRobots, 'nObsidianRobots': nObsidianRobots, 'nGeodeRobots': nGeodeRobots,
                            'ore': ore + nOreRobots - blueprint['oreRobot']['oreCost'], 'clay': clay + nClayRobots,
                            'obsidian': obsidian + nObsidianRobots, 'geode': geode + nGeodeRobots})

    if ore >= blueprint['clayRobot']['oreCost']:
        newStates.append({'nOreRobots': nOreRobots, 'nClayRobots': nClayRobots + 1, 'nObsidianRobots': nObsidianRobots, 'nGeodeRobots': nGeodeRobots,
                            'ore': ore + nOreRobots - blueprint['clayRobot']['oreCost'], 'clay': clay + nClayRobots,
                            'obsidian': obsidian + nObsidianRobots, 'geode': geode + nGeodeRobots})

    if ore >= blueprint['obsidianRobot']['oreCost'] and clay >= blueprint['obsidianRobot']['clayCost']:
        newStates.append({'nOreRobots': nOreRobots, 'nClayRobots': nClayRobots, 'nObsidianRobots': nObsidianRobots + 1, 'nGeodeRobots': nGeodeRobots,
                            'ore': ore + nOreRobots - blueprint['obsidianRobot']['oreCost'], 'clay': clay + nClayRobots - blueprint['obsidianRobot']['clayCost'],
                            'obsidian': obsidian + nObsidianRobots, 'geode': geode + nGeodeRobots})

    if ore >= blueprint['geodeRobot']['oreCost'] and obsidian >= blueprint['geodeRobot']['obsidianCost']:
        newStates.append({'nOreRobots': nOreRobots, 'nClayRobots': nClayRobots, 'nObsidianRobots': nObsidianRobots, 'nGeodeRobots': nGeodeRobots + 1,
                            'ore': ore + nOreRobots - blueprint['geodeRobot']['oreCost'], 'clay': clay + nClayRobots,
                            'obsidian': obsidian + nObsidianRobots - blueprint['geodeRobot']['obsidianCost'], 'geode': geode + nGeodeRobots})
    
    return newStates

def stateGoodness(state, blueprint):
    return (state['clay'] + blueprint['obsidianRobot']['clayCost'] * state['obsidian'] +
            blueprint['obsidianRobot']['clayCost'] * blueprint['geodeRobot']['obsidianCost'] * state['geode']
            + state['nClayRobots'] + blueprint['obsidianRobot']['clayCost'] * state['nObsidianRobots']
            + blueprint['obsidianRobot']['clayCost'] * blueprint['geodeRobot']['obsidianCost'] * state['nGeodeRobots'])

def qualityLevel(max):
    return max[0] * max[1]

maxes = []

for key,blueprint in blueprints.items():
    print(f'--- Blueprint {key} ---')
    states = [startState]
    for minute in range(24):
        print(minute + 1, len(states))
        states = list(reduce(lambda a,b: a + b, [generateFutureStates(state, blueprint) for state in states]))
        if minute >= 9:
            states.sort(key=lambda state: stateGoodness(state, blueprint), reverse=True)
            states = states[:2000]
    maxes.append((max(states, key=lambda state: state['geode'])['geode'], key))
    print(max(states, key=lambda state: state['geode']))
    print('---')

print(sum(map(qualityLevel, maxes)))