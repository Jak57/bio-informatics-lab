def de_bruijn(kmers):
  dic = {}
  for kmer in kmers:
    prefix = kmer[:-1]
    suffix = kmer[1:]
    if prefix not in dic.keys():
      dic[prefix] = [suffix]
    else:
      dic[prefix].append(suffix)

  for k in dic:
    print(k + " -> ", end="")
    for j, item in enumerate(dic[k]):
      if j+1 == len(dic[k]):
        print(item, end="")
      else:
        print(item, end=",")
    print()

if __name__ == "__main__":
  kmers = [
    "GAGG",
    "CAGG",
    "GGGG",
    "GGGA",
    "CAGG",
    "AGGG",
    "GGAG"
  ]

  # with open('rosalind_ba3e.txt') as file:
  #   kmers = file.read().strip().split("\n")
  de_bruijn(kmers)
