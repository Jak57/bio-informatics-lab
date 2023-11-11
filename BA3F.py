def eulerian_cycle(graph):
  def visit(node):
    while graph[node]:
      neighbor = graph[node].pop()
      visit(neighbor)
    cycle.append(node)
  
  cycle = []
  visit(list(graph.keys())[0])
  return cycle[::-1]

if __name__ == "__main__":
  graph = {}
  with open('rosalind_ba3f.txt') as file:
    f = file.read().strip().split("\n")

    for f1 in f:
      tmp = f1.split(" -> ")
      node = tmp[0]
      edges = tmp[1].split(",")
      graph[node] = edges

  cycle = eulerian_cycle(graph)
  cycle = [str(n) for n in cycle]
  print("->".join(cycle))
