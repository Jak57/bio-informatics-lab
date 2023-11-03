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

def score(peptide, spectrum_e):
  spectrum_t = theoretical_spectrum(peptide)
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

def expand(leader_board):
  amino_acids = MASS.keys()
  expanded_leader_board = []

  for peptide in leader_board:
    choices = amino_acids
    for amino_acid in choices:
      expanded_leader_board.append(peptide+amino_acid)
  return expanded_leader_board

def mass(peptide):
  total = 0
  for ch in peptide:
    total += MASS[ch]
  return total

def parent_mass(spectrum):
  x = sorted(spectrum)
  return x[-1]

def cut(leader_board, spectrum, n):
  high = []
  for peptide in leader_board:
    score_p = score(peptide, spectrum)
    high.append((score_p, peptide))

  high = sorted(high, reverse=True)
  if len(high) <= n:
    new_leader_board = []
    for t in high:
      new_leader_board.append(t[1])
    return new_leader_board

  mx_val = high[n-1][0]
  new_leader_board = []
  for t in high:
    if t[0] >= mx_val:
      new_leader_board.append(t[1])
  return new_leader_board

def leader_board_cyclopeptide_sequencing(spectrum, n):
  leader_board = [""]
  leader_peptide = ""

  cnt = 0
  while len(leader_board) > 0:
    leader_board = expand(leader_board)

    for peptide in leader_board:
      if mass(peptide) == parent_mass(spectrum):
        if score(peptide, spectrum) > score(leader_peptide, spectrum):
          leader_peptide = peptide
      elif mass(peptide) > parent_mass(spectrum):
        leader_board = [p for p in leader_board if not(p == peptide)]

    leader_board = cut(leader_board, spectrum, n)
  return leader_peptide

if __name__ == "__main__":
  n = 10
  spectrum_e = [0, 71, 113, 129, 147, 200, 218, 260, 313, 331, 347, 389, 460]

  with open('/content/rosalind_ba4g.txt', "r") as file:
    f = file.read().strip().split()
    n = int(f[0])
    f1 = f[1:]
    spectrum_e = []
    for val in f1:
      spectrum_e.append(int(val))

  leader_peptide = leader_board_cyclopeptide_sequencing(spectrum_e, n)
  values = [str(MASS[ch]) for ch in leader_peptide]
  print("-".join(values))
