def hamming_distance(dna, p):
  cnt = 0
  for i in range(len(p)):
    if not(dna[i] == p[i]):
      cnt += 1
  return cnt

def distance_between_pattern_and_string(pattern, dnas):
  k = len(pattern)
  distance = 0
  for dna in dnas:
    hamming_dist = 10000000

    for i in range(len(dna) - k + 1):
      sub = dna[i:i+k]
      if hamming_dist > hamming_distance(sub, pattern):
        hamming_dist = hamming_distance(sub, pattern)

    distance = distance + hamming_dist
  return distance

pattern = "AAA"
dnas = ["TTACCTTAAC", "GATATCTGTC", "ACGGCGTTCG", "CCCTAAAGAG", "CGTCAGAGGT"]
distance = distance_between_pattern_and_string(pattern, dnas)
print(distance)

