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

for index, i in enumerate(permutations):
    permutations[index] = "".join(map(str, i))

output = []

for element in permutations:
    string = str(element)
    intermediate = []
    for char in string:
        if char == "1":
            char = "Unesco"
        elif char == "2":
            char = "Kulübü"
        elif char == "3":
            char = "Tarih"
        elif char == "4":
            char = "Panosu"
        else:
            char = str(char)
        intermediate.append(char)
        result = " ".join(intermediate)
    output.append(result)

print(output)
print(f"The amount of permutations: {len(output)}")
