def permutation(arr):
    result = []
    if len(arr) == 1:
        return [arr]
    for j in range(len(arr)):
        remaining = arr[:j] + arr[j + 1:]
        sub_per = permutation(remaining)
        for p in sub_per:
            result.append([arr[j]] + p)
    return result


numbers = []
a = int(input("number of elements: "))
for k in range(1, a + 1):
    numbers.append(k)

permutations = permutation(numbers)
print(permutations)
