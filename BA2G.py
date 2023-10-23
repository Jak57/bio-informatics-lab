import math
import random

def hamming_distance(text1, text2):
  cnt = 0
  for i in range(len(text1)):
    if not(text1[i] == text2[i]):
      cnt += 1
  return cnt

def score(motifs, consensus):
  total_score = 0
  for motif in motifs:
    total_score += hamming_distance(motif, consensus)
  return total_score

def consensus_string(motifs):
  k = len(motifs[0])
  c_s = ""
  for i in range(k):
    dic = {
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0
    }

    for motif in motifs:
      ch = motif[i]
      dic[ch] += 1
    mx = max(dic.values())
    for key in dic:
      if mx == dic[key]:
        c_s += key
        break
  return c_s

def get_profile_most_probable_kmer(profile, dna, k, t):
  frequency_matrix = profile.copy()
  for key in frequency_matrix:
    frequency_matrix[key] = [(val+1)/(t+4) for val in frequency_matrix[key]]

  n = len(dna)
  kmer_list = []
  max_score = -1.0
  for i in range(n-k+1):
    score = 1.0
    kmer = dna[i:i+k]

    for j, ch in enumerate(kmer):
      score *= frequency_matrix[ch][j]
    max_score = max(max_score, score)
    kmer_list.append((kmer, score))

  for kmer in kmer_list:
    if max_score == kmer[1]:
      return kmer[0]

def create_profile(motifs, k):
  matrix = {
      'A': [0]*k,
      'C': [0]*k,
      'G': [0]*k,
      'T': [0]*k
  }
  for motif in motifs:
    for i, ch in enumerate(motif):
      matrix[ch][i] += 1
  return matrix

def randomized_motif_search_with_pseudocount_and_gibbs_sampling(dnas, k, t, N):
  best_score = math.inf
  n = len(dnas[0])
  motifs = []

  for dna in dnas:
    idx = random.randint(0, n-k)
    motifs.append(dna[idx:idx+k])
  best_motifs = motifs.copy()

  for j in range(N):
    i = random.randint(0, t-1)
    motifs = motifs[:i] + motifs[i+1:]
    profile = create_profile(motifs, k)
    next_motif = get_profile_most_probable_kmer(profile, dnas[i], k, len(motifs))

    motifs.insert(i, next_motif)
    consensus = consensus_string(motifs)
    score_motif = score(motifs, consensus)

    if score_motif < best_score:
      best_score = score_motif
      best_motifs = motifs

  return best_motifs, best_score

if __name__ == "__main__":
  k, t, N = 8, 5, 100
  dnas = [
    "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
    "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
    "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
    "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
    "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
  ]

  # with open('rosalind_ba2g.txt') as file:
  #   f = file.read().strip().split("\n")
  #   first = f[0].split()
  #   k = int(first[0])
  #   t = int(first[1])
  #   N = int(first[2])
  #   dnas = f[1:]

  best_motifs, best_score = randomized_motif_search_with_pseudocount_and_gibbs_sampling(dnas, k, t, N)
  for i in range(1,20):
    motif, _score = randomized_motif_search_with_pseudocount_and_gibbs_sampling(dnas, k, t, N)
    if _score < best_score:
      best_motifs = motif
      best_score = _score

  for motif in best_motifs:
    print(motif)
