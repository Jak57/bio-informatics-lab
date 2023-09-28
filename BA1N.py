def create(s, kmers):
  if len(s) == n:
    kmers.append(s)
    return s
  create(s+'A', kmers)
  create(s+'C', kmers)
  create(s+'G', kmers)
  create(s+'T', kmers)

def mismatch(dna, p, n, d):
  cnt = 0
  for i in range(n):
    if not(dna[i] == p[i]):
      cnt += 1
  return (cnt <= d)

if __name__ == "__main__":
  dna = "TAGACAACCT"
  d = 3
  n = len(dna)
  kmers = []
  create('', kmers)
  candidate_kmers = []

  for kmer in kmers:
    if (mismatch(kmer, dna, len(kmer), d)):
      candidate_kmers.append(kmer)

  for kmer in candidate_kmers:
    print(kmer)
