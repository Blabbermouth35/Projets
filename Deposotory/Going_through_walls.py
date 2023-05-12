# You have a 69% chance to run through walls, if you fail, the % Drops by 0.5%, if you do it, the % Rises by 1%.

import random
import matplotlib.pyplot as plt

x = []
y = [69.0, ]


def run():
    percentage = 690
    print(percentage / 10)
    while percentage < 1000:
        if random.randint(1, 100) * 10 > percentage:
            percentage -= 5
            y.append(percentage / 10)
        else:
            percentage += 10
            if percentage < 1005:
                y.append(percentage / 10)
        if percentage > 1000:
            print(100)
            y.append(100.0)
        else:
            print(percentage / 10)


run()

for i in range(len(y)):
    x.append(i)

plt.xlabel('Tries')
plt.ylabel('Result Percentage')
plt.title('You have a 69% chance to go through walls, if you fail, it Drops by 0.5%, if you do it, it Rises by 1%')
plt.step(x, y)
plt.grid(True)
plt.show()
