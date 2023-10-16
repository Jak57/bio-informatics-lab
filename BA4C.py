

if __name__ == "__main__":
  p = "MWLGMVPTYKHR"
  q = p + p[:-1]
  all = [p]

  dic = {
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

  n = len(q)
  m = len(p)
  for i in range(n-m+1):
    for j in range(m):
      sub = q[i:i+j]
      if len(sub) > 0:
        all.append(q[i:i+j])

  ans = [0]
  for p in all:
    val = 0
    for ch in p:
      val += dic[ch]
    ans.append(val)

  ans = sorted(ans)
  for i in ans:
    print(i, end=" ")
