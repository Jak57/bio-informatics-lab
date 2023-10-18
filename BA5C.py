def path(X, Y, position, i, j, ans):
  while (i > 0 and j > 0):
    if position[i][j] == 'D':
      ans += X[i]
      i -= 1
      j -= 1
    elif position[i][j] == 'U':
      i -= 1
    elif position[i][j] == 'L':
      j -= 1
  return ans

def LCS(X, Y, dp):
  n = len(X)
  m = len(Y)
  position = []
  for i in range(n):
    position.append(['o']*m)

  for i in range(1, n):
    for j in range(1, m):
      if X[i] == Y[j]:
        dp[i][j] = dp[i-1][j-1]+1
        position[i][j] = 'D'
      elif dp[i][j-1] > dp[i-1][j]:
        dp[i][j] = dp[i][j-1]
        position[i][j] = 'L'
      else:
        dp[i][j] = dp[i-1][j]
        position[i][j] = 'U'

  ans = path(X, Y, position, n-1, m-1, ans="")
  print(ans[::-1])

if __name__ == "__main__":
  X = "AACCTTGG"
  Y = "ACACTGTGA"

  with open('rosalind_ba5c.txt') as file:
    f = file.read().split()
    X = f[0]
    Y = f[1]

  X = "D" + X
  Y = "P" + Y
  n = len(X)
  m = len(Y)

  dp = []
  for i in range(n):
    dp.append([0]*m)
  LCS(X, Y, dp)
