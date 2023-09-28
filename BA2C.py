dna = "ACATTCGGTCAGCCTGGACATAATCCCCAGAGACGCCCCAGACCTCAATAACACAAATTGCGAGATGATAAAAATAGAAGGTGTAGCAAAAACGATAAGCCTTCCCAGAGGGTGGTTAAAGTGTTCTATCCAGTCGCCGGCGGTGGGCCATGCCGAAACTCTGGAGTGTGCCTTAAGACATGCCAAAGAGCAACGGAGGG"
k = 6
dic = {
    'A': [0.212, 0.303, 0.303, 0.333, 0.242, 0.091],
    'C': [0.273, 0.212, 0.182, 0.242, 0.212, 0.303],
    'G': [0.364, 0.182, 0.333, 0.212, 0.333, 0.242],
    'T': [0.152, 0.303, 0.182, 0.212, 0.212, 0.364]
}

kmers = set()
n = len(dna)
for i in range(n-k+1):
  kmers.add(dna[i:i+k])

kmers = sorted(list(kmers))
ans = []
dic_kmer = {}

for kmer in kmers:
  small_ans = 1.0
  for i, base in enumerate(kmer):
    small_ans *= (dic[base][i])
  ans.append(small_ans)
  dic_kmer[kmer] = small_ans

mn = max(ans)
for k in dic_kmer:
  if dic_kmer[k] == max(ans):
    print(k)
    break
