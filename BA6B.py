def count_breakpoints(numbers):
    n = len(numbers)
    total = 0
    for i in range(n-1):
        num1 = numbers[i]
        num2 = numbers[i+1]
        if num1>= 0 and num2 >= 0 and num2-num1 == 1:
            continue
        elif num1 < 0 and num2 < 0 and (num2-num1) == 1:
            continue
        total += 1
    return total

if __name__ == "__main__":
    # permutation = "(+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14)"

    with open('rosalind_ba6b.txt') as file:
        permutation = file.read().strip()

    permutation = permutation[1:-1].split(" ")
    numbers = [0]
    mx = -1
    for ch in permutation:
        mx = max(mx, abs(int(ch)))
        numbers.append(int(ch))

    numbers.append(mx+1)
    total = count_breakpoints(numbers)
    print(total)
