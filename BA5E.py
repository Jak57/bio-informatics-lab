def path(X, Y, position, i, j):
  x = ""
  y = ""
  while  i > 0 and j > 0:
    if position[i][j] == 'D':
     # if X[i] == Y[j]:
      x += X[i]
      y += Y[j]
      i -= 1
      j -= 1
    elif position[i][j] == 'U':
      x += X[i]
      y += "-"
      i -= 1
    elif position[i][j] == 'L':
      x += "-"
      y += Y[j]
      j -= 1

  if i > 0:
    while i > 0:
      x += X[i]
      i -= 1
      y += "-"
  elif j > 0:
    while j > 0:
      y += Y[j]
      j -= 1
      x += "-"
  return x, y

def global_alignment(X, Y, indel):
  X = '1' + X
  Y = '1' + Y
  n = len(X)
  m = len(Y)

  item = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
  dic = {}
  for i in range(len(item)):
    for j in range(len(item)):
      key = item[i] + item[j]
      dic[key] = indel[i][j]

  dp = []
  for i in range(n):
    dp.append([0]*m)

  gap = -5
  dp[0][0] = 0
  for i in range(1, n):
    dp[i][0] = dp[i-1][0] + gap

  for i in range(1, m):
    dp[0][i] = dp[0][i-1] + gap

  position = []
  for i in range(n):
    position.append(['o']*m)

  for i in range(n):
    position[i][0] = 'U'

  for i in range(m):
    position[0][i] = 'L'

  for i in range(1, n):
    for j in range(1, m):
      a = dp[i-1][j] + gap
      b = dp[i][j-1] + gap

      key = X[i] + Y[j]
      c = dp[i-1][j-1] + dic[key]
      mx = max(max(a, b), c)
      dp[i][j] = mx

      if mx == c:
        position[i][j] = 'D'
      elif mx == a:
        position[i][j] = 'U'
      else:
        position[i][j] = 'L'

  x, y = path(X, Y, position, n-1, m-1)
  score = dp[n-1][m-1]
  x = x[::-1]
  y = y[::-1]
  return score, x, y

if __name__ == "__main__":
  X = "PLEASANTLY"
  Y = "MEANLY"
  indel = [[4, 0, -2, -1, -2, 0, -2, -1, -1, -1, -1, -2, -1, -1, -1, 1, 0, 0, -3, -2], [0, 9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2], [-2, -3, 6, 2, -3, -1, -1, -3, -1, -4, -3, 1, -1, 0, -2, 0, -1, -3, -4, -3], [-1, -4, 2, 5, -3, -2, 0, -3, 1, -3, -2, 0, -1, 2, 0, 0, -1, -2, -3, -2], [-2, -2, -3, -3, 6, -3, -1, 0, -3, 0, 0, -3, -4, -3, -3, -2, -2, -1, 1, 3], [0, -3, -1, -2, -3, 6, -2, -4, -2, -4, -3, 0, -2, -2, -2, 0, -2, -3, -2, -3], [-2, -3, -1, 0, -1, -2, 8, -3, -1, -3, -2, 1, -2, 0, 0, -1, -2, -3, -2, 2], [-1, -1, -3, -3, 0, -4, -3, 4, -3, 2, 1, -3, -3, -3, -3, -2, -1, 3, -3, -1], [-1, -3, -1, 1, -3, -2, -1, -3, 5, -2, -1, 0, -1, 1, 2, 0, -1, -2, -3, -2], [-1, -1, -4, -3, 0, -4, -3, 2, -2, 4, 2, -3, -3, -2, -2, -2, -1, 1, -2, -1], [-1, -1, -3, -2, 0, -3, -2, 1, -1, 2, 5, -2, -2, 0, -1, -1, -1, 1, -1, -1], [-2, -3, 1, 0, -3, 0, 1, -3, 0, -3, -2, 6, -2, 0, 0, 1, 0, -3, -4, -2], [-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2, 7, -1, -2, -1, -1, -2, -4, -3], [-1, -3, 0, 2, -3, -2, 0, -3, 1, -2, 0, 0, -1, 5, 1, 0, -1, -2, -2, -1], [-1, -3, -2, 0, -3, -2, 0, -3, 2, -2, -1, 0, -2, 1, 5, -1, -1, -3, -3, -2], [1, -1, 0, 0, -2, 0, -1, -2, 0, -2, -1, 1, -1, 0, -1, 4, 1, -2, -3, -2], [0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1, 0, -1, -1, -1, 1, 5, 0, -2, -2], [0, -1, -3, -2, -1, -3, -3, 3, -2, 1, 1, -3, -2, -2, -3, -2, 0, 4, -3, -1], [-3, -2, -4, -3, 1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11, 2], [-2, -2, -3, -2, 3, -3, 2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1, 2, 7]]
  # with open('rosalind_ba5e.txt') as file:
  #   f = file.read().split()
  #   X = f[0]
  #   Y = f[1]

  score, x_align, y_align = global_alignment(X, Y, indel)
  print(score)
  print(x_align)
  print(y_align)


##### Have to find other opitmal paths too (bonus)
