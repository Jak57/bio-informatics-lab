dic = {
    0: 'A',
    1: 'C',
    2: 'G',
    3: 'T'
}

def number_to_pattern(index, k):
  if k == 1:
    return dic[index]

  last_idx = index%4
  last_char = dic[last_idx]
  prefix = index//4
  return number_to_pattern(prefix, k-1) + last_char

print(number_to_pattern(5200, 7))
