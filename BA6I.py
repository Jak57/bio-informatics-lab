def cycle_to_chromosome(nodes):
    n = len(nodes)
    chromosome = []
    for i in range(0, n, 2):
        if nodes[i] < nodes[i+1]:
            chromosome.append(nodes[i+1]//2)
        else:
            chromosome.append(-nodes[i]//2)
    return chromosome

def graph_to_genome(graph):
    n = len(graph)
    cycles = []
    temp = []

    for i in range(n):
        if i == n-1:
            temp.append(graph[i][0])
            temp.append(graph[i][1])
            cycles.append(temp)
        elif graph[i][1] == graph[i+1][0]+1 or graph[i][1] == graph[i+1][0]-1:
            temp.append(graph[i][0])
            temp.append(graph[i][1])
        else:
            temp.append(graph[i][0])
            temp.append(graph[i][1])
            cycles.append(temp)
            temp = []

    p = []
    for cycle in cycles:
        nodes = [cycle[-1]] + cycle[:-1]
        chromosome = cycle_to_chromosome(nodes)
        p.append(chromosome)
    return p


if __name__ == "__main__":
    text = "(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)"

    with open("rosalind_ba6i.txt") as file:
        text = file.read().strip()

    text = text[:-1]
    text = text.split("), ")
    edges = []
    for item in text:
        item = item[1:].split(", ")
        edges.append([int(item[0]), int(item[1])])

    ans = graph_to_genome(edges)
    for item in ans:
        genome = "("
        for i in item:
            if i > 0:
                x = '+' + str(i) + " "
            else:
                x = '-' + str(abs(i)) + " "
            genome += x

        genome = genome.strip() + ")"
        print(genome, end=" ")
