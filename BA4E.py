MASS = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]

def cyclospectrum_mass_peptide(peptide):
    spec = [0, calculate_mass(peptide)]
    temp = peptide + peptide
    for k in range(1, len(peptide)):
        for i in range(len(peptide)):
            subpeptide = temp[i:i + k]
            spec.append(calculate_mass(subpeptide))
    spec.sort()
    return spec

def linear_spectrum(peptide):
  n = len(peptide)
  spec = []

  for i in range(n):
    sum = 0
    for j in range(i, n):
      sum += peptide[j]
      spec.append(sum)
      
  sum = 0
  for i in range(n-2):
    sum += peptide[i]
    spec.append(sum)
  return sorted(spec)

def consistent(peptide, spectrum):
  if calculate_mass(peptide) > spectrum[-1] - MASS[0]:
    return False
  spec = linear_spectrum(peptide)

  for p in spec:
    if p not in spectrum:
      return False
  return True

def expand(peptides):
  new_peptides = []
  for m in MASS:
    for peptide in peptides:
      new_peptides.append(peptide + [m])
  return new_peptides

def calculate_mass(peptide):
  total = 0
  for i in peptide:
    total += i
  return total

def cyclopeptide_sequencing(spectrun):
  peptides = [[]]
  cnt = 0
  ans = []

  while peptides:
    peptides = expand(peptides)
    parent_mass = spectrun[-1]
    for peptide in peptides:

      if calculate_mass(peptide) == parent_mass:
        if cyclospectrum_mass_peptide(peptide) == spectrum:
          ans.append(peptide)
        peptides = [p for p in peptides if p != peptide]
      elif not consistent(peptide, spectrum):
        peptides = [p for p in peptides if p != peptide]
  return ans

if __name__ == "__main__":
  spectrum = [0, 113, 128, 186, 241, 299, 314, 427]

  with open('rosalind_ba4e.txt') as file:
    f = file.read().strip().split()
    spectrum = [int(val) for val in f]

  ans = cyclopeptide_sequencing(spectrum) 
  for s in ans:
    new_s = [str(val) for val in s]
    print("-".join(new_s), end=" ")
  print()
