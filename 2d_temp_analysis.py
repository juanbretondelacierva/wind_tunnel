import numpy as np
import os
from matplotlib import pyplot as plt

aoa = ["-3","-2","-1","0","1","2","3","3.5","4","4.5","5","5.5","6","6.5","7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12","12.5","13","13.5","14","14.5","15","15.5","16","16.5","17","17.5","18","17.5h","17h","16.5h","16h","15.5h","15h","14.5h","14h","13.5h","13h","12.5h","12h","11.5h"]

def plot():
    for foulder in aoa:
        data_matrix = np.asmatrix(np.zeros((480, 640)))
        for filename in os.listdir("2D/"+str(foulder)+"/"):
            number_of_files = len([name for name in os.listdir("2D/"+str(foulder)+"/") if os.path.isfile(os.path.join("2D/"+str(foulder)+"/", name))])
            data_array = np.matrix(np.loadtxt(open("2D/"+str(foulder)+"/"+filename, "rb"), delimiter=";", usecols=range(640)))
            data_matrix += data_array/number_of_files
        fig, ax = plt.subplots()
        fig.suptitle(f"Angle of Attack "+str(foulder))
        im = ax.imshow(data_matrix, cmap="jet")
        fig.colorbar(im, ax=ax, label='Interactive colorbar')
        plt.show()
    

plot()