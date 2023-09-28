k, d = 5, 1
dnas = [
  "GCTGCATTTTGGTCGGGTCCTCTAC",
  "GCTCCGATAGCGCCTCAATATGGTA",
  "CTATGTGTCTGTTCCTTCCGAGGGT",
  "ATAACCGCGCTATCGCGAAAGATCC",
  "GGCGGACTTCTGGCACGACAGTTCC",
  "GAACTGTCTAGTTGCGCTCCGACAC",
  "GATCCAACACACTTTGTCTTCTTTA",
  "AAACTAGAATGCTCCGGTCCTGCGG",
  "TTCGCACCGTGTTCCCTTGAGGTAT",
  "AGCCGGAGTCGTTCCGGACGCCGCG",
]

def create(s, kmers):
  if len(s) == k:
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

kmers = []
create('', kmers)

def present_all(kmer, dnas):
  ans = []
  for dna in dnas:
    for i in range(len(dna) - k + 1):
      sub = dna[i:i+k]
      if mismatch(sub, kmer, k, d):
        ans.append(1)
        break
  return len(ans) == len(dnas)

ans = []
for kmer in kmers:
  if present_all(kmer, dnas):
    ans.append(kmer)

for p in ans:
  print(p, end=" ")
