def de_bruijn(k, text):
  n = len(text)
  dic = {}
  k -= 1
  for i in range(n-k):
    kmer = text[i:i+k]
    adj = text[i+1:i+k+1]

    if kmer not in dic.keys():
      dic[kmer] = [adj]
    else:
      dic[kmer].append(adj)

  for k in dic:
    print(k + " -> ", end="")
    for j, item in enumerate(dic[k]):
      if j+1 == len(dic[k]):
        print(item, end="")
      else:
        print(item, end=",")
    print()


if __name__ == "__main__":
  k = 4
  text = "AAGATTCTCTAC"
  # with open('rosalind_ba3d.txt') as file:
  #   f = file.read().strip().split("\n")
  #   k = int(f[0])
  #   text = f[1]
  de_bruijn(k, text)
