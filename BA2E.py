import math

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

def greedy_motif_search_with_pseudocount(dnas, k, t):
  best_motifs = []
  best_score = math.inf
  for dna in dnas:
    best_motifs.append(dna[:k])

  n = len(dnas[0])
  first_dna = dnas[0]
  for i in range(n-k+1):
    motifs = [first_dna[i:i+k]]

    for j in range(1, t):
      profile = create_profile(motifs, k)
      profile_most_probable_kmer = get_profile_most_probable_kmer(profile, dnas[j], k,  t)
      motifs.append(profile_most_probable_kmer)

    consensus = consensus_string(motifs)
    score_motif = score(motifs, consensus)
    if score_motif < best_score:
      best_score = score_motif
      best_motifs = motifs
      
  return best_motifs

if __name__ == "__main__":
  # k, t = 3, 5
  # dnas = [
  #   "GGCGTTCAGGCA",
  #   "AAGAATCAGTCA",
  #   "CAAGGAGTTCGC",
  #   "CACGTCAATCAC",
  #   "CAATAATATTCG"
  # ]

  with open('rosalind_ba2e.txt') as file:
    f = file.read().split("\n")
    first = f[0].split()
    k = int(first[0])
    t = int(first[1])
    dnas = f[1:]

  motifs = greedy_motif_search_with_pseudocount(dnas, k, t)
  for motif in motifs:
    print(motif)
