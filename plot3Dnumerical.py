import matplotlib.pyplot as plt
import numpy as np
import os

def convertarrayandplot(data, label = ''):
    x, y = [item[0] for item in data], [item[1] for item in data]

    plt.plot(x, y, marker='.', label=label)
    return

for filename in os.listdir('.\\Numerical3D'):
    data_LTT = np.loadtxt(open(os.path.join('.\\Numerical3D', filename), "rb"), delimiter=",", usecols=[0, 1], skiprows=1, max_rows=42)
    data_Panel = np.loadtxt(open(os.path.join('.\\Numerical3D', filename), "rb"), delimiter=",", usecols=[3, 4], skiprows=1)
    data_VLM = np.loadtxt(open(os.path.join('.\\Numerical3D', filename), "rb"), delimiter=",", usecols=[6, 7], skiprows=1)

    convertarrayandplot(data_LTT, label = 'LTT')
    convertarrayandplot(data_Panel, label = 'Panel Method')
    convertarrayandplot(data_VLM, label = 'VLM')
    
    plt.title(f"{filename}")
    plt.grid()
    plt.legend()
    plt.show()
