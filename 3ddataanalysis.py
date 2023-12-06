import numpy as np
import os
import copy
import matplotlib.pyplot as plt

#data = [np.loadtxt(f'\\3D\\{i}') for i in range(-3, 13)]

# Initialize dictionary with keys as folder names
data = {key:[] for key in os.listdir('.\\3D')}

for directory in os.listdir('.\\3D'):
    #folderarray = np.zeros(len(os.listdir(f'.\\3D\\{directory}')))
    folderarray = np.asmatrix(np.zeros((480, 640)))
    print(f'Current directory: {directory}')

    for i, filename in enumerate(os.listdir(f'.\\3D\\{directory}')):
        with open(os.path.join(f'.\\3D\\{directory}', filename)) as f: # open in readonly mode
            folderarray += np.matrix(np.loadtxt(f, delimiter=';', usecols=range(640)))
    
    folderarray /= (i+1)
    data[directory] = copy.deepcopy(folderarray)


#print(data['0'])
fig, ax = plt.subplots()
im = ax.imshow(data['0'])
fig.colorbar(im, ax=ax, label='Interactive colorbar')

plt.show()