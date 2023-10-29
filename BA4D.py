def total_peptide(total, masses):
  m = len(masses)
  dp = [0] * (total+1)
  dp[0] = 1

  for i in range(total+1):
    cursum = 0
    for j in range(m):
      if i - masses[j] >= 0:
        cursum += dp[i-masses[j]]
    dp[i] += cursum
  return dp[total]

if __name__ == "__main__":
  total = 1307
  masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
  
  # with open('rosalind_ba4d.txt') as file:
  #   f = file.read().strip().split()
  #   total = int(f[0])

  total_ways = total_peptide(total, masses)
  print(total_ways)
