def limb_length(distance_matrix, i, n):
    d = []
    for j in range(n):
        for k in range(n):
            dist = (distance_matrix[i][k] + distance_matrix[i][j] - distance_matrix[j][k])//2
            if dist > 0:
                d.append(dist)
    return min(d)

if __name__ == "__main__":
    with open('rosalind_ba7b.txt') as file:
        f = file.read().strip().split("\n")
        n = int(f[0])
        j = int(f[1])
        other = f[2:]
        arr2d = []*n

        for item in other:
            item = item.split(" ")
            tmp = []
            for num in item:
                if len(num) > 0:
                    tmp.append(int(num))
            arr2d.append(tmp)

        length = limb_length(arr2d, j, n)
        print(length)

"""
input:
-----
4
1
0   13  21  22
13  0   12  13
21  12  0   13
22  13  13  0

output:
------
2
"""
