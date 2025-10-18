import matplotlib.pyplot as plt

ivme_bas = float(input("Başlangıç ivmesi: "))
ivme_art = float(input("İvme saniyede artış dercesi: "))
t = float(input("Hız Sınırı: "))
h = float(input("Başlangıç Hızı: "))
zaman = [0, 1]
i = 1
m = h
a = ivme_bas
ivme = [0, a]
hiz = [0, h]
metre = [0, h]
while True:
    a += ivme_art
    if h > t:
        break
    h += a
    hiz.append(h)
    ivme.append(a)
    i += 1
    zaman.append(i)
    m += h
    metre.append(m)


plt.xlabel('Zaman')
plt.ylabel('m/s - m/s2')
plt.title("İvme-Hız-Metre")

plt.step(zaman, ivme, label='İvme')
plt.plot(zaman, hiz, label='Hız')
plt.plot(zaman, metre, label='Metre')

plt.grid(True)
plt.legend()
plt.show()
