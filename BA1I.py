from collections import defaultdict

def neighbor(pattern, mismatch, candidate_kmers):
  bases = ['A', 'T', 'G', 'C']
  for i in range(len(pattern)):
    for j in range(len(bases)):
      new_kmer = pattern[:i] + bases[j] + pattern[i+1:]
      if (mismatch <= 1):
        candidate_kmers.add(new_kmer)
      else:
        neighbor(new_kmer, mismatch-1, candidate_kmers)

dna = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k, d = 4, 1
n = len(dna)
ans = defaultdict(int)

for i in range(n-k+1):
  candidate_kmers = set()
  sub = dna[i:i+k]
  neighbor(sub, d, candidate_kmers)

  for kmer in candidate_kmers:
    ans[kmer] += 1

mx = max(ans.values())
for k in ans:
  if mx == ans[k]:
    print(k, end=" ")
