import networkx as nx
import re
import matplotlib.pyplot as plt
from itertools import permutations, combinations


def loadData():
    G = nx.Graph()
    with open('aoc16.txt', 'r') as f:
        for line in f.readlines():
            valve = re.findall('([A-Z]{2}).+?(\d+)', line.strip())[0]
            leads = re.split('valves? ', line.strip())[1].split(', ')
            for v in leads:
                G.add_node(valve[0], **{'flow': int(valve[1]), 'open': 'False'})
                G.add_edge(valve[0], v, **{'weight': 1})
    for valve in list(G):
        if valve not in G or valve == 'AA':
            continue
        if not G.nodes[valve]['flow']:
            for u in G[valve]:
                for v in G[valve]:
                    if u == v:
                        continue
                    G.add_edge(u, v, **{'weight': G[valve][u]['weight'] + G[valve][v]['weight']})
            G.remove_node(valve)
    return G


def totalFlow(G: nx.classes.graph, path: list[str], min: int = 30) -> int:
    total = 0
    for v, valve in enumerate(path):
        if v == 0:
            continue
        min -= nx.shortest_path_length(G, valve, path[v - 1], weight='weight')
        min -= 1
        if min <= 0:
            break
        G.nodes[valve]['open'] = True
        total += min * G.nodes[valve]['flow']
    return total


def totalLength(G: nx.classes.graph, path: list[str]) -> int:
    length = 0
    for i, j in zip(path[1:], path[:-1]):
        length += nx.shortest_path_length(G, i, j, weight='weight')
    return length


G = loadData()
plt.cla()
nx.draw(G, pos=nx.spring_layout(G), node_color=['b' if G.nodes[n]['flow'] else 'r' for n in G], with_labels=True)

allPaths = []
nodes_combs = combinations(G.nodes, 2)

for source, target in nodes_combs:
    paths = nx.all_simple_paths(G, source=source, target=target, cutoff=30)
    for path in paths:
        if path not in allPaths and path[::-1] not in allPaths:
            allPaths.append(path)
for path in allPaths:
    print(path, totalFlow(G, list(path), 30))
print(max(totalFlow(G, list(path), 30) for path in allPaths))

selfPaths = [path for path in allPaths if totalFlow(G, list(path), 26) and path[0] == 'AA']
elephantPaths = selfPaths

exclusion = []
for selfPath in selfPaths:
    for elephantPath in elephantPaths:
        if any(i in selfPath[1:] for i in elephantPath[1:]):
            continue
        else:
            exclusion.append((selfPath, elephantPath))
            print(len(exclusion))

<<<<<<< HEAD
print(max(
    totalFlow(G, list(selfPath), 26) + totalFlow(G, list(elephantPath), 26) for selfPath, elephantPath in exclusion))
=======
print(max(totalFlow(G, list(selfPath), 26) + totalFlow(G, list(elephantPath), 26) for selfPath, elephantPath in exclusion))
>>>>>>> 5cb5d696050000f143756d95f59cb15ee28a3ab1
