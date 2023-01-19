import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

x1 = (1, 2, 3)
y1 = (0, 0, 0)

plt.plot(x1, y1)

x2 = (1, 2, 3)
y2 = (3, 3, 3)

plt.plot(x2, y2)

plt.show()