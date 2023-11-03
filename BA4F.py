MASS = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113,
    'N': 114,
    'D': 115,
    'K': 128,
    'Q': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186,
    'L': 113,
}

def theoretical_spectrum(peptide):
  n = len(peptide)
  spectrum = [peptide]
  peptide += peptide
  m = len(peptide)

  for i in range(n):
    for j in range(i, i+n-1):
      spectrum.append(peptide[i:j+1])

  weights = [0]
  for p in spectrum:
    w = 0
    for ch in p:
      w += MASS[ch]
    weights.append(w)
  return sorted(weights)

def calculate_score(spectrum_e, spectrum_t):
  dic_t = {}
  dic_e = {}
  for num in spectrum_t:
    if num not in dic_t.keys():
      dic_t[num] = 1
    else:
      dic_t[num] += 1

  for num in spectrum_e:
    if num not in dic_e.keys():
      dic_e[num] = 1
    else:
      dic_e[num] += 1

  score = 0
  for k in dic_e:
    if k in dic_t.keys():
      score += min(dic_e[k], dic_t[k])
  return score

if __name__ == "__main__":
  peptide = "NQEL"
  spectrum_e = [0, 99, 113, 114, 128, 227, 257, 299, 355, 356, 370, 371, 484]

  with open('rosalind_ba4f.txt') as file:
    f = file.read().strip().split()
    peptide = f[0]
    f1 = f[1:]
    spectrum_e = []
    for n in f1:
      spectrum_e.append(int(n))

  spectrum_t = theoretical_spectrum(peptide)
  score = calculate_score(spectrum_e, spectrum_t)
  print(score)
