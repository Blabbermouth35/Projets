import matplotlib.pyplot as plt
import random

x = []
y = []


def dice(z):
    for j in range(z):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        y.append(d1 + d2)


a = int(input("How many times do they roll?\n: "))
for i in range(a + 1):
    x.append(i)
x.remove(0)

dice(a)
plt.plot(x, y)
plt.show()
