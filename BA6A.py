def reversal(pattern, i, j):
  start, end = i, j
  while i < j:
    tmp = pattern[i]
    pattern[i] = pattern[j]
    pattern[j] = tmp
    i += 1
    j -= 1

  for idx in range(start, end+1):
    pattern[idx] = -pattern[idx]

def print_pattern(pattern):
  print("(", end="")
  for i in range(len(pattern)):
    if i == len(pattern)-1:
      if pattern[i] > 0:
        print("+", end="")
      print(pattern[i], end=")\n")
      break

    if pattern[i] > 0:
      print("+", end="")
    print(pattern[i], end=" ")

def greedy_sorting(pattern):
  n = len(pattern)
  for i in range(n):
    for j in range(i, n):
      if abs(pattern[j]) == i+1:
        if i == j and pattern[j] > 0:
          continue
        reversal(pattern, i, j)
        print_pattern(pattern)

    if pattern[i] < 0:
      pattern[i] = -pattern[i]
      print_pattern(pattern)

if __name__ == "__main__":
  with open('rosalind_ba6a.txt') as file:
    x = file.read().strip()

  x = x[1:len(x)-1]
  y = x.split(" ")

  pattern = []
  for ch in y:
    sign = ch[0]
    i = ch[1:]
    num = int(i)
    if sign == '-':
      num = -num
    pattern.append(num)
  greedy_sorting(pattern)
