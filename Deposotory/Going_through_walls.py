# You have a 69% chance to run through walls, if you fail, the % Drops by 0.5%, if you do it, the % Rises by 1%.

import random


def run():
    percentage = 690
    print(percentage / 10)
    while percentage < 1000:
        if random.randint(1, 100) * 10 > percentage:
            percentage -= 5
        else:
            percentage += 10
        if percentage > 1000:
            print(100)
            break
        else:
            print(percentage / 10)


run()
