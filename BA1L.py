dic = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}

def pattern_to_number(pattern):
  if len(pattern) < 1:
    return 0
  last = pattern[-1]
  prefix = pattern_to_number(pattern[:-1])
  return (4*prefix + dic[last])

print(pattern_to_number("GGTCACCGGGGGGGCTGCATCGCTAGGGCT"))
