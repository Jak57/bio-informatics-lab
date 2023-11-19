def chromosome_to_cycle(chromosome):
    n = len(chromosome)
    nodes = [0]*(2*n+1)

    for j in range(1, n+1):
        i = chromosome[j-1]
        if i > 0:
            nodes[2*j-1] = 2*i - 1
            nodes[2*j] = 2*i
        else:
            nodes[2*j-1] = -2*i
            nodes[2*j] = -2*i-1
    return nodes[1:]

def colored_edges(p):
    n = len(p)
    edges = []
    for chromosome in p:
        m = len(chromosome)
        nodes = chromosome_to_cycle(chromosome)
        nodes_ = [0] + nodes + [nodes[0]]

        for j in range(1, m+1):
            edges.append((nodes_[2*j], nodes_[2*j+1]))
    return edges


if __name__ == "__main__":
    text = "(+1 -2 -3)(+4 +5 -6)"    
    with open('rosalind_ba6h.txt') as file:
        text = file.read().strip()
    
    text = text.split("(")[1:]
    p = []
    for item in text:
        item = item[:-1].split()
        item = [int(ch) for ch in item]
        p.append(item)

    ans = colored_edges(p)
    print(str(ans)[1:-1])
