k = 6
dnas = [
"GGATCTTGCTGTATGGGAGGGTAACTGTAGTTGGAGTTTAGG",
"TAATGGCTGTAATATGCCATAAACATCTGAGACTTAATGACC",
"TCGTTGGTTCCTCTTAACGTTATTCTGTAGCGTGCTGCACCC",
"CGGGGACTAACGATTTTCCTGTACTCGGAGCTGCCGTGGCCG",
"CTGTATCCGACGGCCCGTGATTCGCGATACTGTGACTGACAT",
"GTTCGCCCTCAACGTTGACTGTACGTACGCATCGGTATAATC",
"CCGTAACTGTAAAAAGGGTACCTGCCTCTTTAGACAAGAATC",
"AGCTTCCTGTAAGACAGCTGGCTTGTCTAGTATTGGACTCTA",
"AGACTTCTGTAAAGTTGACCCTCTGTTAAAAAAATTACCATC",
"TCCTTTCCTGCTCTGTAGAGTGAGCACACTGTAAGAAGACGT"
]

def create(s, kmers):
  if len(s) == k:
    kmers.append(s)
    return s
  create(s+'A', kmers)
  create(s+'C', kmers)
  create(s+'G', kmers)
  create(s+'T', kmers)

def hamming_distance(dna, p):
  cnt = 0
  for i in range(len(p)):
    if not(dna[i] == p[i]):
      cnt += 1
  return cnt


def min_distance(dna, kemr):
  n = len(dna)
  dis = []
  k = len(kmer)
  for i in range(n-k+1):
    sub = dna[i:i+k]
    dis.append(hamming_distance(sub, kmer))

  return min(dis)

def find_mn_distance(dnas, kmer):
  sum_d = 0
  for dna in dnas:
    mn_d = min_distance(dna, kmer)
    sum_d += mn_d
  return sum_d

kmers = []
create('', kmers)
global_mn = 100000000
dic = {}

for kmer in kmers:
  mn = find_mn_distance(dnas, kmer)
  dic[kmer] = mn
  global_mn = min(global_mn, mn)

for k in dic:
  if dic[k] == global_mn:
    print(k)
    break
