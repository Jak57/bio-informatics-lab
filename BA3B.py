def reconstruction(dnas):
  s = dnas[0]
  n = len(dnas)
  for i in range(1, n):
    last = dnas[i]
    s += last[len(last)-1]
  return s;

if __name__ == "__main__":
  with open('rosalind_ba3b.txt') as file:
    dnas = file.read().strip().split("\n")
  print(reconstruction(dnas))
