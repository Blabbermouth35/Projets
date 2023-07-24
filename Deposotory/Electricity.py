import matplotlib.pyplot as plt
import numpy as np

saatler = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
uretim = [0.5, 1.2, 2.0, 3.1, 4.2, 4.8, 4.9, 4.5, 3.8, 2.9, 1.8, 0.9]

m, b = np.polyfit(saatler, uretim, 1)

saatler_array = np.array(saatler)
y_pred = m * saatler_array + b

plt.plot(saatler, uretim, marker='o', label='kWh')
plt.plot(saatler, y_pred, color='blue', label='Doğrusal Regresyon')

plt.xlabel('Saat')
plt.ylabel('Elektrik Üretimi (kWh)')
plt.title('Güneş Panelinden Saate Göre Elektrik Üretimi')
plt.xticks(saatler)
plt.grid(True)

plt.legend()

plt.show()
