def manhattan_grid(down, right, n, m):
  n += 1
  m += 1
  dp = []
  for i in range(n):
    temp = [0] * m
    dp.append(temp)

  for i in range(1, n):
    dp[i][0] = dp[i-1][0] + down[i-1][0]
  for j in range(1, m):
    dp[0][j] = dp[0][j-1] + right[0][j-1]

  for col in range(1, m):
    for row in range(1, n):
      dp[row][col] = max(dp[row][col-1]+right[row][col-1], dp[row-1][col]+down[row-1][col])
  return dp[n-1][m-1]

if __name__ == "__main__":
  with open('rosalind_ba5b.txt') as file:
    f = file.read().split("\n")
    t1 = f[0]
    t1 = t1.split()
    n = int(t1[0])
    m = int(t1[1])
    t2 = f[1:n+1]
    t3 = f[n+2:]

    down = []
    for c in t2:
      temp = []
      t = c.split()
      for i in t:
        temp.append(int(i))
      down.append(temp)

    right = []
    for c in t3:
      temp = []
      t = c.split()
      for i in t:
        temp.append(int(i))
      right.append(temp)
    
    longest_path = manhattan_grid(down, right, n, m)
    print(longest_path)
