def reverse_complement(text):
    dic = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A'
    }
    text = text[::-1]
    new_text = ""
    for ch in text:
        new_text += dic[ch]
    return new_text


def shared_kmers(k, text1, text2):
    n = len(text1)
    m = len(text2)

    dic1 = {}
    for i in range(n-k+1):
        sub = text1[i:i+k]
        rev = reverse_complement(sub)
        if sub in dic1.keys():
            dic1[sub].append(i)
        elif rev in dic1.keys():
            dic1[rev].append(i)
        else:
            dic1[sub] = [i]

    shared = []
    for i in range(m-k+1):
        sub = text2[i:i+k]
        rev = reverse_complement(sub)
        if sub in dic1.keys():
            for j in dic1[sub]:
                shared.append((i, j))
        elif rev in dic1.keys():
            for j in dic1[rev]:
                shared.append((i, j))
    return shared


if __name__ == "__main__":
    k = 3
    text1 = "AAACTCATC"
    text2 = "TTTCAAATC"

    with open('rosalind_ba6e (2).txt') as file:
        f = file.read().strip().split("\n")
        k = int(f[0])
        text1 = f[1]
        text2 = f[2]

    shared = shared_kmers(k, text1, text2)
    for v in shared:
        print("(" + str(v[1]) + ", " + str(v[0]) + ")")
