import operator

ops = {"+": operator.add, "-": operator.sub, "x": operator.mul, "/": operator.truediv}

a = int(input(":"))
b = int(input(":"))
c = input(":")

print(ops[c](a, b))
