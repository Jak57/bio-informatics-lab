from Bio.Seq import Seq

def reverse_complement(text):
  d = {
      'A': 'T',
      'T': 'A',
      'G': 'C',
      'C': 'G'
  }
  text = text[::-1]
  ans = ""
  for ch in text:
    ans += d[ch]
  return ans

option = []
if __name__ == "__main__":
  text = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
  p = "MA"

  # with open('rosalind_ba4b.txt') as file:
  #   f = file.read().strip().split()
  #   text = f[0]
  #   p = f[1]
  kmers = []
  k = len(p) * 3
  n = len(text)

  for i in range(n-k+1):
    sub = text[i:i+k]
    kmers.append(text[i:i+k])
    if (Seq(p) == Seq(sub).translate() or Seq(p) == Seq(reverse_complement(sub)).translate()):
      print(sub)

