def eulerian_cycle(graph, source):
  def visit(node):
    while graph[node]:
      neighbor = graph[node].pop()
      visit(neighbor)
    cycle.append(node)

  cycle = []
  visit(source)
  return cycle[::-1]

if __name__ == "__main__":
  graph = {
    0: [2],
    1: [3],
    2: [1],
    3: [0, 4],
    6: [3, 7],
    7: [8],
    8: [9],
    9: [6]
  }

  graph = {}
  with open('rosalind_ba3g.txt') as file:
    f = file.read().strip().split("\n")

    for f1 in f:
      tmp = f1.split(" -> ")
      node = tmp[0]
      edges = tmp[1].split(",")
      graph[int(node)] = [int(e) for e in edges]

  all = set()
  for k in graph:
    all.add(k)
    for val in graph[k]:
      all.add(val)

  all = sorted(list(all))
  in_degree = {}
  out_degree = {}
  for k in all:
    in_degree[k] = 0
    out_degree[k] = 0

  for k in graph:
    out_degree[k] = len(graph[k])

  for k in graph:
    neighbor = graph[k]
    for node in neighbor:
      in_degree[node] += 1

  cycle = True
  for k in in_degree.keys():
    if out_degree[k] - in_degree[k] == 1:
      source = k
    if in_degree[k] - out_degree[k] == 1:
      destination = k
    if out_degree[k] == 0:
      cycle = False

  if not cycle:
    graph[destination] = [source]

  c = eulerian_cycle(graph, source)
  if not cycle:
    c = [str(n) for n in c][:-1]
  else:
    c = [str(n) for n in c]
  print("->".join(c))
