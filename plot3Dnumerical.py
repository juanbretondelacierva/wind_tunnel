import matplotlib.pyplot as plt
import numpy as np
import os


#function that converts csv files directly into a specific plot of points, 
#having the data, the linetyle, the marker style and the label as variables
def convertarrayandplot(data, trace, dot, label = ''):
    x, y = [item[0] for item in data], [item[1] for item in data] #retrieves values x,y of the dataset
    plt.plot(x, y, linestyle=trace ,marker=dot, label=label)
    return

#looks into all files in the folder of numerical, and for each file it creates a plot of the three analysis methods
for filename in os.listdir('.\\Numerical3D'):
    data_LTT = np.loadtxt(open(os.path.join('.\\Numerical3D', filename), "rb"), delimiter=",", usecols=[0, 1], skiprows=1 , max_rows=42) 
    data_Panel = np.loadtxt(open(os.path.join('.\\Numerical3D', filename), "rb"), delimiter=",", usecols=[3, 4], skiprows=1)
    data_VLM = np.loadtxt(open(os.path.join('.\\Numerical3D', filename), "rb"), delimiter=",", usecols=[6, 7], skiprows=1)

    convertarrayandplot(data_LTT, "-",".", label = 'LTT')
    convertarrayandplot(data_Panel, ":","", label = 'Panel Method')
    convertarrayandplot(data_VLM, ":","", label = 'VLM')
    # Set the x-axis label
    plt.xlabel('X-Drag Coefficient [-]')

    # Set the y-axis label
    plt.ylabel('Y-Lift Coefficient [-]')
    
    
    plt.title(f"{filename}")
    plt.grid()
    plt.legend()
    plt.show()
