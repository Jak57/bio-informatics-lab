from collections import defaultdict
from queue import Queue

def bfs(src, graph):
    d = [-1]*len(graph)
    d[src] = 0
    q = Queue()
    q.put(src)

    while not q.empty():
        parent = q.get()
        for child, weight in graph[parent]:
            if d[child] == -1:
                d[child] = d[parent] + weight
                q.put(child)
    return d

if __name__ == "__main__":
    with open('rosalind_ba7a.txt') as file:
        f = file.read().strip().split("\n")
        n = int(f[0])
        other = f[1:]
    
    graph = defaultdict(list)
    for item in other:
        s, o = item.split('->')
        e, w = o.split(":")
        w = int(w)
        graph[int(s)].append([int(e), w])

    for i in range(n):
        src = i
        ans = bfs(src, graph)[:n]
        print(" ".join([str(ch) for ch in ans]))

"""
input
-------
4
0->4:11
1->4:2
2->5:6
3->5:7
4->0:11
4->1:2
4->5:4
5->4:4
5->3:7
5->2:6

output
------
0 13 21 22
13 0 12 13
21 12 0 13
22 13 13 0
"""
