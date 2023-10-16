def kmer_composition(k, text):
  n = len(text)
  kmers = []
  for i in range(n-k+1):
    kmers.append(text[i:i+k])
  return sorted(kmers)

if __name__ == "__main__":
  k = 5
  text = "CAATCCAAC"

  # with open('rosalind_ba3a.txt') as file:
  #   f = file.read().split("\n")
  #   k = int(f[0])
  #   text = f[1]

  kmers = kmer_composition(k, text)
  for kmer in kmers:
    print(kmer)
