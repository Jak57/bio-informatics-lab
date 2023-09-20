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

def reverse_complement(pattern):
  pattern = pattern[::-1]
  dic = {
      'A': 'T',
      'C': 'G',
      'G': 'C',
      'T': 'A',
  }
  rev_c = ""
  for ch in pattern:
    rev_c += dic[ch]
  return rev_c

dna = "CAGCACTTTCCCCCCATCAGCACTTCAGCACTTGGTCACCATACCCTTCAGCACTTGGTCACCCAGCACTTTCCCCCCATCAGCACTTCAGCACTTGCGAATGCAGCACTTTCCCCCCATGGTCACCATACCCTTATACCCTTTCCCCCCATTCCCCCCATCAGCACTTTCCCCCCATCAGCACTTCAGCACTTGCGAATGGGTCACCGGTCACCGGTCACCATACCCTTGGTCACCTCCCCCCATGCGAATGGCGAATGATACCCTTCAGCACTTATACCCTTTCCCCCCATATACCCTTCAGCACTTGCGAATGCAGCACTTCAGCACTTGCGAATGTCCCCCCATATACCCTTGCGAATGCAGCACTTCAGCACTTTCCCCCCATTCCCCCCATGCGAATGGCGAATGTCCCCCCATATACCCTTTCCCCCCATGGTCACCCAGCACTTATACCCTTTCCCCCCATTCCCCCCATATACCCTTGGTCACCATACCCTTCAGCACTTGGTCACCATACCCTTCAGCACTTGCGAATGCAGCACTTTCCCCCCATGGTCACCGGTCACCGCGAATGCAGCACTTGGTCACCGCGAATGGCGAATGGGTCACCATACCCTTCAGCACTTGCGAATGTCCCCCCATGGTCACCGGTCACCTCCCCCCATGGTCACCTCCCCCCATATACCCTTGGTCACCCAGCACTTGGTCACCGGTCACCGGTCACCCAGCACTTGGTCACCTCCCCCCATCAGCACTTGCGAATGGCGAATGCAGCACTTGCGAATGGCGAATGATACCCTTTCCCCCCATCAGCACTTGCGAATGTCCCCCCATTCCCCCCATATACCCTTATACCCTT"
k, d = 6, 3

n = len(dna)
ans = defaultdict(int)

for i in range(n-k+1):
  candidate_kmers = set()
  sub = dna[i:i+k]
  neighbor(sub, d, candidate_kmers)

  for kmer in candidate_kmers:
    ans[kmer] += 1

  candidate_kmers = set()
  neighbor(reverse_complement(sub), d, candidate_kmers)
  for kmer in candidate_kmers:
    ans[kmer] += 1

mx = max(ans.values())
for k in ans:
  if mx == ans[k]:
    print(k, end=" ")
