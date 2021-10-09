import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-deep')

[33, 37, 8, 8, 4, 33]
[33, 37, 8, 4]
num_repeats40 =[2, 1, 2, 1]
num_repeats = [1, 3, 2, 16, 26, 40, 39, 53, 57, 37, 35, 30, 21, 17, 10, 3, 3, 3, 2, 2 ]
num_impuls = ('1', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '22')
bins = np.linspace(0, 22, 22)
plt.hist([num_repeats, num_repeats40], bins)
plt.show()    

