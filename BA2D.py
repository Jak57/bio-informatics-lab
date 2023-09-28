import math

def profile_most_probable_kmer(dna, k, profile):

  dic = profile
  kmers = []
  n = len(dna)
  for i in range(n-k+1):
    kmers.append(dna[i:i+k])

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
      return k

def create_profile(motifs):
  k = len(motifs[0])
  profile = {
      'A': [0]*k,
      'C': [0]*k,
      'G': [0]*k,
      'T': [0]*k,
  }

  for i in range(len(motifs)):
    for j, base in enumerate(motifs[i]):
      profile[base][j] += 1
  return profile


def consensus_string(motifs):
  c_s = ""
  for i in range(len(motifs[0])):
    dic = {
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0
    }

    for motif in motifs:
      dic[motif[i]] += 1

    mx = max(dic.values())
    for k in dic:
      if mx == dic[k]:
        c_s += k
        break

  return c_s

def hamming_distance(dna, p):
  cnt = 0
  for i in range(len(p)):
    if not(dna[i] == p[i]):
      cnt += 1
  return cnt

def score(consensus_motif, motifs):
  total_score = 0.0
  for motif in motifs:
    d = hamming_distance(consensus_motif, motif)
    total_score += d
  return total_score

def greedy_motif_search(dnas, k, t):
  best_motifs = []
  best_score = math.inf

  for dna in dnas:
    best_motifs.append(dna[:k])

  first_dna = dnas[0]
  n = len(first_dna)

  for i in range(n-k+1):
    motifs = []
    motifs.append(first_dna[i:i+k])

    for j in range(1, t):
      profile = create_profile(motifs)

      frequency_profile = profile.copy()
      for key in frequency_profile:
        frequency_profile[key] = [val/t for val in frequency_profile[key]]

      next_choice = profile_most_probable_kmer(dnas[j], k, frequency_profile)
      motifs.append(next_choice)

    consensus_motif = consensus_string(motifs)
    score_motif = score(consensus_motif, motifs)

    if score_motif < best_score:
      best_motifs = motifs
      best_score = score_motif

  return best_motifs

DNA = [
"GGCGTTCAGGCA",
"AAGAATCAGTCA",
"CAAGGAGTTCGC",
"CACGTCAATCAC",
"CAATAATATTCG"
]

k, t = 3, 5
motifs = greedy_motif_search(DNA, k, t)
for motif in motifs:
  print(motif)
