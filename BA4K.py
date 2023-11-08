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

def generate_linear_spectrum(mass):
  for i in range(1, len(mass)):
    mass[i] += mass[i-1]

  ans = [0]
  for i in range(len(mass)-1):
    for j in range(i+1, len(mass)):
      ans.append(mass[j]-mass[i])
  return sorted(ans)

def compute_score(spectrum_given, spectrum_pred):
  dic1 = {}
  dic2 = {}
  for v in spectrum_given:
    if v not in dic1.keys():
      dic1[v] = 0
    dic1[v] += 1

  for v in spectrum_pred:
    if v not in dic2.keys():
      dic2[v] = 0
    dic2[v] += 1

  score = 0
  for k in dic1:
    if k in dic2.keys():
      score += min(dic1[k], dic2[k])
  return score

if __name__ == "__main__":
  linear_spectrum_given = []
  with open('rosalind_ba4k.txt', "r") as file:
    f = file.read().strip().split()
    peptide = f[0]
    text = f[1:]
    for ch in text:
      linear_spectrum_given.append(int(ch))

  mass = [0]
  for ch in peptide:
    mass.append(MASS[ch])
  linear_spectrum_pred = generate_linear_spectrum(mass)
  score = compute_score(linear_spectrum_given, linear_spectrum_pred)
  print(score)
