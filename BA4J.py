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

if __name__ == "__main__":
  peptide = "MPYENCCCWMFNIRKGQPDFFRKGAVPYVVPMNCIRWS"
  with open('rosalind_ba4j.txt', "r") as file:
    peptide = file.read().strip()

  mass = [0]
  for ch in peptide:
    mass.append(MASS[ch])
  linear_spectrum = generate_linear_spectrum(mass)
  for m in linear_spectrum:
    print(m, end=" ")
