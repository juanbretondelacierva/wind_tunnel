import numpy as np
import os
import copy
import matplotlib.pyplot as plt


data = {key:[] for key in os.listdir('.\\3D')}

print('Gathering Data...')

for directory in os.listdir('.\\3D'):
    #folderarray = np.zeros(len(os.listdir(f'.\\3D\\{directory}')))
    folderarray = np.asmatrix(np.zeros((480, 640)))

    for i, filename in enumerate(os.listdir(f'.\\3D\\{directory}')):
        with open(os.path.join(f'.\\3D\\{directory}', filename)) as f: # open in readonly mode
            folderarray += np.matrix(np.loadtxt(f, delimiter=';', usecols=range(640)))
    
    folderarray /= (i+1)
    data[directory] = copy.deepcopy(folderarray)

print('Data Gatehred')

for key, value in zip(data.keys(), data.values()):
    fig, ax = plt.subplots()
    fig.suptitle(f"Angle of Attack {key}")
    im = ax.imshow(value, cmap='jet')
    fig.colorbar(im, ax=ax, label='Interactive colorbar')

    plt.show()