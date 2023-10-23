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

def randomized_motif_search_with_pseudocount(dnas, k, t):
  best_score = math.inf
  n = len(dnas[0])
  motifs = []

  for dna in dnas:
    idx = random.randint(0, n-k)
    motifs.append(dna[idx:idx+k])
  best_motifs = motifs.copy()

  while True:
    profile = create_profile(motifs, k)
    motifs.clear()
    for j in range(len(dnas)):
      profile_most_probable_kmer = get_profile_most_probable_kmer(profile, dnas[j], k,  t)
      motifs.append(profile_most_probable_kmer)

    consensus = consensus_string(motifs)
    score_motif = score(motifs, consensus)
    if score_motif < best_score:
      best_score = score_motif
      best_motifs = motifs
    else:
      return best_motifs, best_score

if __name__ == "__main__":
  k, t = 8, 5
  dnas = [
    "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
    "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
    "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
    "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
    "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
  ]

  # with open('rosalind_ba2f.txt') as file:
  #   f = file.read().strip().split("\n")
  #   first = f[0].split()
  #   k = int(first[0])
  #   t = int(first[1])
  #   dnas = f[1:]

  best_motifs, best_score = randomized_motif_search_with_pseudocount(dnas, k, t)
  for i in range(1,1000):
    motif, _score = randomized_motif_search_with_pseudocount(dnas, k, t)
    if _score < best_score:
      best_motifs = motif
      best_score = _score
  
  for motif in best_motifs:
    print(motif)
