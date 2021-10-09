import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-deep')

a=[17, 16, 26, 11, 22,16,19,19,17,23,24,19,18,25,17,20,17,26,27,23,
     21,18,24,16,29,11,15,22,24,24,23,32,18,26,22,20,28,23,16,30,
     29,15,16,18,27,17,14,17,25,15,24,22,19,13,25,27,20,19,15,23,
     16,16,26,22,19,19,17,20,17,21,21,14,24,28,20,19,21,23,18,27,
     31,24,25,13,22,22,23,23,21,18,21,16,18,15,14,18,22,18,26,17,
     13,15,17,30,20,25,16,27,20,20,13,20,26,30,21,20,13,23,17,13,
     15,24,16,18,28,25,25,19,20,24,19,18,20,18,22,28,15,19,17,16,
     25,14,26,13,22,19,31,17,22,17,26,22,24,24,26,23,25,22,21,16,
     17,19,21,18,15,24,15,19,17,18,26,19,22,19,21,17,17,27,25,21,
     15,17,14,29,16,18,17,15,20,15,24,20,22,18,21,21,12,18,18,19] #данные для интервалов 20сек
b=[]
for i in range(len(a)):
    if i%2==0:
        c=a[i]
    else:
        b.append(a[i]+c)
print(b)

def get_unique_numbers(numbers):
    unique = []

    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique

num_impuls=get_unique_numbers(b)
num_impuls.sort()
print(num_impuls)

def get_quantity_unique(unique, numbers):
    quantity = []

    for i in range(len(unique)):
        char = unique[i]
        quantity.append(numbers.count(char)/100)
    return quantity

num_repeats = get_quantity_unique(num_impuls, b)
print(num_repeats)

y_pos = np.arange(len(num_impuls))
plt.bar(y_pos, num_repeats, align='center', alpha=1, color='red')
plt.xticks()

plt.ylabel('Доля случаев')
plt.xlabel('Число импульсов')
plt.title('Число срабатываний счётчика за 40 сек')

'''ДЛЯ СОВМЕСТНОГО ПОСТРОЕНИЯ
num_repeats10 = [1, 3, 2, 16, 26, 40, 39, 53, 57, 37, 35, 30, 21, 17, 10, 3, 3, 3, 2, 2 ]
for i in range(len(num_repeats10)):
    num_repeats10[i] = num_repeats10[i]/400'''

'''num_impuls10 = ('1', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '22')
y_pos10 = np.arange(len(num_impuls10))
plt.bar( y_pos10, num_repeats10, align='center', alpha=0.5)
plt.xticks( )

'''

'''ПОПЫТКА НЕ ПЫТКА
colors = ['b','g']
#sets up the axis and gets histogram data
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.hist([num_repeats, num_repeats10], color=colors)
n, bins, patches = ax1.hist([num_repeats,num_repeats10])
ax1.cla() #clear the axis

#plots the histogram data
width = (bins[1] - bins[0]) * 0.4
bins_shifted = bins + width
ax1.bar(bins[:-1], n[0], width, align='edge', color=colors[0])
ax2.bar(bins_shifted[:-1], n[1], width, align='edge', color=colors[1])

#finishes the plot
ax1.set_ylabel("Count", color=colors[0])
ax2.set_ylabel("Count", color=colors[1])
ax1.tick_params('y', colors=colors[0])
ax2.tick_params('y', colors=colors[1])
plt.tight_layout()'''

plt.show()
