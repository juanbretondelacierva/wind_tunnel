import numpy as np
import os
import copy
import pickle
import pandas as pd

if __name__ == '__main__':

    listdir = ["-3","-2","-1","0","1","2","3","4",
           "5","6","7","7.5","8","8.5","9","9.5",
           "10","10.5","11","11.5","12","12.5","13","13.5",
           "14","14.5","15","15.5","16","16.5","17","17.5",
           "18","17.5h","17h","16.5h","16h","15.5h","15h",
           "14.5h","14h","13.5h","13h","12.5h","12h","11.5h"]

    data = {key:None for key in listdir}
    
    right_limit = 446 # 640 or 446 
    left_limit = 196 # 0 or 196

    print('Gathering Data...')

    for directory in listdir:

        folderarray = np.zeros((480, right_limit-left_limit))

        for i, filename in enumerate(os.listdir(f'.\\3D\\{directory}')):
            with open(os.path.join(f'.\\3D\\{directory}', filename)) as f: # open in readonly mode
                folderarray += np.loadtxt(f, delimiter=';', usecols=range(left_limit, right_limit))
        
        folderarray /= (i+1)
        data[directory] = copy.deepcopy(folderarray)

    with open('saved_variables_3d.pkl', 'wb') as file:
        pickle.dump(data, file)
    
    print('Data Gatehred')