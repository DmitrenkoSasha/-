import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.size'] = 16 # Управление стилем, в данном случаем - размером шрифта 
 # Создаем фигуру
plt.figure(figsize=(8,8))

# Функция преобр. долей в мВ
def conv(U):
    for i in range(len(U)):
        U[i] *= 5
    return(U)
#Функция нахожд. прямой по МНК
def MNK(U, I):
    up = 0
    down = 0
    up2 = 0
    down2 = 0
    for i in range(len(U)):
        up+=U[i]*I[i]
        down+=I[i]**2
        up2+=U[i]**2
        down2+=I[i]**2
    k=up/down
    print(k, 1/np.sqrt(10)*np.sqrt(up2/down2-k**2))
    x= np.arange(0, 235, 10)
    y = k*x
    plt.plot(x,y)



# Подписываем оси и график
plt.title(r"Зависимость U(I)")
plt.xlabel("I, mA")
plt.ylabel("U, mV")

U50 = [80, 85, 95, 100, 106, 115, 75, 70, 65, 60]
I50 = [80, 86, 95, 103, 106, 115, 75, 71, 67, 62]
plt.plot(I50, conv(U50), 'ro', label=r'$l=50см, Rср=4.95\pm0.026 Ом$')

#Ещё данных 
U30 = [74.0, 80.0, 50.0, 45.0, 43.0, 55.0, 72.0, 75.0, 85.0, 95.0, 100.0]
I30 = [123, 132, 78, 75, 70, 90, 119, 124, 137, 157, 166 ]
plt.plot(I30, conv(U30), 'r^', label=r'$l=30см, Rср=3.040\pm0.019 Ом$')

#Ещё данных
U20 = [67, 72, 79, 85, 90, 56, 60, 50, 45, 40, 35]
I20 = [168, 179, 195, 209, 230, 139, 150, 125, 110, 99, 86]
plt.plot(I20, conv(U20), 'bs', label=r'$l=20см, Rср=2.01\pm0.012 Ом$')
#plt.errorbar(I20,U20, yerr=5, xerr=1, fmt='.', label='Кресты') 
#Строим прямую по МНК
MNK(U20, I20)
MNK(U30, I30)
MNK(U50, I50)

# Активируем сетку
plt.grid(b=True, which='major', axis='both', alpha=1)
plt.grid(b=True, which='minor', axis='both', alpha=0.5)

plt.legend()
plt.show()
