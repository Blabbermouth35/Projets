import matplotlib.pyplot as plt

a = int(input(': '))

hiz_y = []

for i in range(a + 1):
    hiz_y.append(i)


hiz_x = []

for i in range(a + 1):
    hiz_x.append(i)

plt.plot(hiz_x, hiz_y, label='Hız')

ivme_x = []

for i in range(a):
    ivme_x.append(i)

ivme_x.append(a)

ivme_y = [1]

for i in range(a):
    ivme_y.append(1)

plt.step(ivme_x, ivme_y, label='İvme')

plt.xlabel('Zaman')

plt.ylabel('m/s - m/s2')

plt.title('İvme-Hız')

plt.legend()

plt.show()
