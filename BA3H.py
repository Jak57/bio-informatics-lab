def reconstruction(k, kmers):
  dic = {}
  for kmer in kmers:
    key = kmer[:-1]
    dic[key] = kmer[1:]

  for kmer in dic.keys():
    if kmer not in dic.values():
      first = kmer
      break

  current = first
  ans = current
  while current in dic.keys():
    ans += dic[current][-1]
    current = dic[current]
  return ans

if __name__ == "__main__":
  k = 4
  text = "CTTA ACCA TACC GGCT GCTT TTAC"

  with open('rosalind_ba3h.txt') as file:
    f = file.read().strip().split("\n")
    k = int(f[0])
    kmers = f[1:]

  ans = reconstruction(k, kmers)
  print(ans)
