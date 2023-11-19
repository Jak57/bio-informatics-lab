def cycle_to_chromosome(nodes):
    m = len(nodes)-1
    n = m//2

    chromosome = [0]*(n+1)
    for j in range(1, n+1):
        if nodes[2*j-1] < nodes[2*j]:
            chromosome[j] = nodes[2*j]//2
        else:
            chromosome[j] = -nodes[2*j-1]//2
    return chromosome[1:]

if __name__ == "__main__":
    nodes = "(1 2 4 3 6 5 7 8)"    
    with open('rosalind_ba6g.txt') as file:
        nodes = file.read().strip()
    
    nodes = nodes[1:-1].split()
    nodes = [int(ch) for ch in nodes]
    nodes = [-1] + nodes
    ans = cycle_to_chromosome(nodes)

    ans_ = []
    for n in ans:
        if n > 0:
            ans_.append('+'+str(n))
        else:
            ans_.append(str(n))
    print("(" + " ".join(ans_) + ")")
