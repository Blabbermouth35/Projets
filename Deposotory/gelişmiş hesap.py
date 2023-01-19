import operator

ops = {"+": operator.add, "-": operator.sub}

a = int(input(":"))
b = int(input(":"))
c = input(":")

print(ops[c](a,b))

