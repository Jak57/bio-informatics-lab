from collections import defaultdict
from copy import deepcopy
from math import inf

def reverse_graph(graph):
    all_nodes = set()
    rev_graph = defaultdict(list)

    for key in graph:
        val = graph[key]
        all_nodes.add(key)
        for item in val:
            all_nodes.add(item['n'])

    for node in all_nodes:
        for item in graph[node]:
            rev_graph[item['n']].append({'n':node, 'w': item['w']})
    return rev_graph

def find_sources(graph):
    rev_graph = reverse_graph(graph)
    sources = []
    for key in graph:
        if len(rev_graph[key]) == 0:
            sources.append(key)
    return sources

def topological_order(graph):
    g = deepcopy(graph)
    candidates = find_sources(g)
    order = []

    while candidates:
        n = candidates[0]
        order.append(n)
        candidates.remove(n)
        g[n] = []
        candidates = list(set(find_sources(g)) - set(order))
    return order

def longest_path(graph, src, sink):
    order = topological_order(graph)
    score = {}
    path = defaultdict(list)

    for node in graph:
        score[node] = -inf

    score[src] = 0
    path[src] = [src]
    rev_graph = reverse_graph(graph)

    for node in order[order.index(src)+1:]:
        if rev_graph[node]:
            scores = []
            for item in rev_graph[node]:
                s = score[item['n']] + item['w']
                scores.append(s)

            score[node] = max(scores)
            i = scores.index(max(scores))
            path[node] = path[rev_graph[node][i]["n"]] + [node]
    return score[sink], path[sink]

if __name__ == "__main__":
    with open('rosalind_ba5d.txt') as file:
        f = file.read().strip().split("\n")
        src = f[0]
        sink = f[1]
        other = f[2:]
    
        graph = defaultdict(list)
        for item in other:
            s, o = item.split("->")
            e, w = o.split(":")
            w = int(w)
            graph[s].append({'n': e, 'w': w})
        score, path = longest_path(graph, src, sink)
        print(score)
        print("->".join(path))
