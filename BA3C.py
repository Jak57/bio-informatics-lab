def prefix(kmer):
  return kmer[:-1]

def suffix(kmer):
  return kmer[1:]

def overlap_graph(kmers):
  for i, kmer in enumerate(kmers):
    adj = []
    for j, kmer_adj in enumerate(kmers):
      if i == j:
        continue

      if suffix(kmer) == prefix(kmer_adj):
        adj.append(kmer_adj)

    if len(adj) == 0:
      continue

    print(kmer, end="")
    for j, k in enumerate(adj):
      print(" -> " + k, end="")
    print()

if __name__ == "__main__":
  kmers = [
      "ATGCG",
      "GCATG",
      "CATGC",
      "AGGCA",
      "GGCAT"
  ]

  # with open('rosalind_ba3c.txt') as file:
  #   kmers = file.read().strip().split("\n")

  overlap_graph(kmers)
