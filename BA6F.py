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

if __name__ == "__main__":
    text = "(+1 -2 -3 +4)"

    with open('rosalind_ba6f.txt') as file:
        text = file.read().strip()
    
    text = text[1:-1].split()
    chromosome = [int(ch) for ch in text]
    nodes = chromosome_to_cycle(chromosome)
    nodes = [str(n) for n in nodes]
    print("(" + " ".join(nodes) + ")")
