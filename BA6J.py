
def two_break_on_genome_graph(graph, i):
    i1, i2, i3, i4 = i[0], i[1], i[2], i[3]

    if [i1, i2] in graph:
        graph.remove([i1, i2])
    else:
        graph.remove([i2, i1])

    if [i3, i4] in graph:
        graph.remove([i3, i4])
    else:
        graph.remove([i4, i3])

    graph.append([i1, i3])
    graph.append([i2, i4])
    graph = sorted(graph)
    return graph

if __name__ == "__main__":
    with open('rosalind_ba6j.txt') as file:
        f = file.read().strip().split("\n")
        f1 = f[0][:-1]
        f1 = f1.split("), ")
        f2 = f[1].split(", ")

        i = [int(ch) for ch in f2]
        colored_edges = []
        for item in f1:
            item = item[1:]
            item = item.split(", ")
            colored_edges.append([int(item[0]), int(item[1])])

        graph = two_break_on_genome_graph(colored_edges, i)
        for i, p in enumerate(graph):
            print("(" + str(p[0]) + ", " + str(p[1]) + ")", end="")
            if i == len(graph)-1:
                continue
            print(", ", end="")
