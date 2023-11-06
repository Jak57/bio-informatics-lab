def convolution(spectrum):
  n = len(spectrum)
  dic = {}
  for i in range(n):
    for j in range(n-1):
      if (j == i):
        break
      diff = int(abs(spectrum[i] - spectrum[j]))

      if diff == 0:
        continue
      if diff in dic.keys():
        dic[diff] += 1
      else:
        dic[diff] = 1

  List = []
  for k in dic:
    List.append((dic[k], k))
  List = sorted(List)
  List = List[::-1]
  
  for t in List:
    val = t[1]
    cnt = t[0]
    for j in range(cnt):
      print(val, end=" ")

if __name__ == "__main__":
  spectrum = [0, 137, 186, 323]
  with open('rosalind_ba4h.txt', "r") as file:
    spectrum = []
    f = file.read().strip().split()
    for val in f:
      spectrum.append(int(val))
  convolution(spectrum)
