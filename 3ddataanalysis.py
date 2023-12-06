import numpy as np
import os

#data = [np.loadtxt(f'\\3D\\{i}') for i in range(-3, 13)]

data = []
for i, filename in enumerate(os.listdir('.\\3D\\0')):
   with open(os.path.join('.\\3D\\0', filename)) as f: # open in readonly mode
      data.append(np.loadtxt(f, delimiter=';', usecols=range(640)))

print(data[0])