import numpy as np
import os
import copy

data = {key:None for key in os.listdir('.\\3D')}

if __name__ == '__main__':

    print('Gathering Data...')

    for directory in os.listdir('.\\3D'):
        #folderarray = np.zeros(len(os.listdir(f'.\\3D\\{directory}')))
        folderarray = np.asmatrix(np.zeros((480, 640)))

        for i, filename in enumerate(os.listdir(f'.\\3D\\{directory}')):
            with open(os.path.join(f'.\\3D\\{directory}', filename)) as f: # open in readonly mode
                folderarray += np.array(np.loadtxt(f, delimiter=';', usecols=range(640)))
        
        folderarray /= (i+1)
        data[directory] = copy.deepcopy(folderarray)

    print('Data Gatehred')