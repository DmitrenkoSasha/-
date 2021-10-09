import numpy as np
import matplotlib.pyplot as plt
import random
plt.style.use('seaborn-deep')

a =[]
for i in range(20000): 
    temp = random.randint(0, 50) 
    a.append(temp)
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


plt.show()
