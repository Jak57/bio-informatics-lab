dna1 = "TGGCCTGTACGGACCGTGCCCAACTTAAAGGAATCTGACCCCTTAACTTGCTCGCCCCCAGCGTGACCTCAATCCTTCCATCCCGCAGTTCGATCTCGTCATGATCCCCATGCCTCATAAATTTTACTGGAGCGGATACCATCTAGATGGGCATACCCAATGTCTACTCCCGGTTTGCTGTGTATGCAACACCTTCGAAGCGGTCTGCATGTGATTGCCATTCAGCCCTCCCACGGTCTTTCGAGTGATCTGGGTAGCAGGTCGATCAACATGGCTGTGCAGTGCCGTCTAGATTTTGAGCGTTGCCGGCAATGTCCGTCGCAACATATAGGCCAAAGTAGGACAGGGTTAGATTCGCGAAGGCGCGTCCCGACTTCTCTCGAGGCGTAGTGCTAGCTTAGAACGTATGACAATTGACTCTGAGCAATGATCCATTTAGGTGGAATGATTATGTTGGATGCGAGGGCACTTTAGCATTGCTCGGCATGCAGAGCACTGATTCGAGCTTGCATGATATAACCACTCTATATCCACAGTGAACGAAGATATCCGCTTATAGCAACCAACGAAGAGGGCCTTTGTAAAGCAATTTCGTGAATGGGCGATGTATCTCCGAATCTCGTCTTATGCGTTCTCGACTTAGAAAGCTCCACCAACCCTACCGTGAGCAGAACTGCCGGGCCACCACGCCCTGGAATAGGTCCATGCAGCCCTTGAGTCCAGCGGATTGGGGAGGAGTCACGCCATACCCAAAGCCGGCTGTACCCCGTAGTTATACCAGAATCTATGCTCTCACCCGGATTTCACTTGTCATCACTCTTCTTCGAACTGTATCATCTAGTAAGCGTGCTAACGGCTACGGGGCATTAATTGTTACTTACCTAAACCGCCTCCTTAGCTGATTAGCCCCCACACCGGTGAGTATAGAAGCTAACTGATGTGTCTCTCCGGTAAACTGAAAACCAACATAGTGCGCCTAGTTCCTCGGCTGGCCGACCAGGATGTCCGGGGGCTTTAAGTATGACCCGGCCTCTTTTTCTGAGTG"
dna2 = "TTCATGTAGACTGGCATCTCTTCCGCTCCGGTGCTAAAGGACTTACGACTTATGGGACTAGTGCCCTGTCAAACCAGATTTTTATGCATCACAACCCGACGAAAATAATCCTCTGCACGAGTGATAAGATGAGAAAGACGACGTTCCGTTTGCTGGCTACGCAGACTACTGAGGTGGCCCCACCATATATCCCCTAGTATGTTGTTCGATAACTTGTTCATCTATATATGTGTTACCCGTGAGGTAGTCTATGCAACCGCTAGATGTCGCTGGCGAGATTCTCACCTAGGTCCAAGTATGGGTTGCCCTGACACATAGTGTGTAATAACAACCTTCTCGCAAAAATATCTGTGCTTTGTGCTTGTCTTAATCCAGTGCCGAGGTCAGACTCCTGCGGATTTGGAGGAAGTCTTGTGATAACTCGACCCGACCCGACCCAGATGTGGATATACGTGAACTATACACATGTCGTTTGCGGGTGAATTTTCTGCACGTATGTGTCACATCGAATCCCAGTGCATAAAATAGGCCCTGATGCTGTATGCCCACAGCCAAATTTATTAGTTATCATCATACCGATTCCATTGTAGCGGACATTAGTAGTCCCTCGCGAAGGCGGATTGGCATGTTACGCTATTTTTTGGCTGTACTCCATTGAGTTCTGAGAAGGTGACGCGCCGGTCGACCGCCTGGCGCCCGTCCGTCGACCCAGCTTGTACCCTTGAGTGGGTCACAAGCCTACTGAACCACGTTGTACTCGGCTTGTCGCGGTGTCAAGTTCCCGAGTTAGTTAAATAGACCACGTAACTTATGTGTAGCCGTCCAGGCAGACGCAGTTGATTCGCTGTGGTATGTACCCCTTTCATCTGGAGTACCTGGGCTACGTCGTGCCAGTGGAGGCCACGGAGGAAAAAAAGATATTCCTATGACAAGACTGCTCTGTTCTTAGGAGGTCCCCACCAGCATAGACCGAGGTTAAATAAGTGCGTGCAAGCACCGTTCGATGTCAGATCCATGAATACAATTTACGCCACGGCTCCAAATA"
n = len(dna1)
m = len(dna2)
mn = min(n, m)

hd = 0
for i in range(mn):
  if not(dna1[i] == dna2[i]):
    hd += 1

print(hd)
