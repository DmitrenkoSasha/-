import numpy as np
import matplotlib.pyplot as plt

num_impuls = ('1', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '22')
y_pos = np.arange(len(num_impuls))
num_repeats = [1, 3, 2, 16, 26, 40, 39, 53, 57, 37, 35, 30, 21, 17, 10, 3, 3, 3, 2, 2 ]

for i in range(len(num_repeats)):
    num_repeats[i] = num_repeats[i]/400

plt.bar(y_pos, num_repeats, align='center', alpha=0.5)
plt.xticks()
plt.ylabel('Доля случаев')
plt.xlabel('Число импульсов')
plt.title('Число срабатываний счётчика за 10 сек')

'''
objects = ('1', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '22')
y_pos = np.arange(len(objects))
performance = [1, 3, 2, 16, 26, 40, 39, 53, 57, 37, 35, 30, 21, 17, 10, 3, 3, 3, 2, 2 ]'''
plt.show()
