
#plt.use('TkAgg')
import collections

import numpy as np
from matplotlib import pyplot as plt
plt.rcdefaults()
import pandas
from array import array

data = pandas.read_csv(r'/home/tequi/CSV/feb18-3pmto5pm.csv')
column3= data.iloc[:,19]
n_array=column3.to_numpy()
freq=collections.Counter(n_array)
no_times_list=[0]*11;
for key, value in freq.items():
    no_times_list[key]=value
no_times_array=array("i",no_times_list)
print(no_times_array)
x_positions = np.arange(0,11)
y_positions = np.arange(1,22,2)
plt.figure()
plt.bar(x_positions,no_times_array,align='center', alpha=0.5)
plt.xticks(x_positions)
plt.yticks(y_positions)
plt.ylabel('Node 10')
plt.xlabel("Infectors")
plt.title('worm infection')
plt.savefig("/home/tequi/histograms/feb18-3pmto5pm/node10.png")