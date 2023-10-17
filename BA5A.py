def coin_change(money, coins, dp):
  for coin in coins:
    for j in range(1, money+1):
      if j >= coin:
        dp[j] = min(dp[j], dp[j-coin]+1)
  return dp[money]


if __name__ == "__main__":
  # money = 40
  # coins = [1, 5, 10, 20, 25, 50]

  with open('rosalind_ba5a.txt') as file:
    f = file.read().split()
    money = int(f[0])
    tmp = f[1].split(',')
    coins = []
    for i in tmp:
      coins.append(int(i))

  dp = []
  inf = int(1e9)
  for i in range(money+1):
    dp.append(inf)
  dp[0] = 0

  mn_coins = coin_change(money, coins, dp)
  print(mn_coins)
