import numpy as np
print("Введите массив данных через пробел\n")

n=[int(i) for i in input().split()]


def sigma(n):
    """Функция считает среднеквадратичную ошибку отдельного измерения
    """
    up = 0
    down = 0
    average = sum(n)/len(n)  # Среднее значение
    for i in range(len(n)):
        up+=(n[i]-average)**2
    down=len(n)
    sigma=np.sqrt(up/down)
    return sigma

print(sigma(n))
