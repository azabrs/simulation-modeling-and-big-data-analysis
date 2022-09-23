import numpy as np
import pandas as pd
array = np.sqrt(np.linspace(0,10,50,endpoint=False))[48::-2]#inverted array of length 50, in which every second element remains
array_2 = np.vstack((array,np.logspace(0,1,25,base=2)))#matrix with extra row
array_3 = np.apply_along_axis(lambda x: np.prod(x)**(1/x.size), 0, array_2)#geometric mean
a=np.mean(array_3)# arithmetic mean of geometric mean 
array_4 = np.array([])
for i in np.linspace(-3,3,1000):
  array_4 = np.append(array_4,np.sinc(i)) if array_4 is not None else np.array(i)

mean_arr = np.mean(array_4)
max_arr = max(array_4)
min_arr = min(array_4)
sko_arr = np.std(array_4)
med_arr = np.median(array_4)
print("Mean = {}\tMax = {}\tMin = {}\tStd = {}\tMedian = {}".format(mean_arr,max_arr,min_arr,sko_arr,med_arr))

