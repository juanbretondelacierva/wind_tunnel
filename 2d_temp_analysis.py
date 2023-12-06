import numpy as np
import os
from matplotlib import pyplot as plt


data_matrix = np.asmatrix(np.zeros((480, 640)))
for filename in os.listdir("2D/0/"):
    number_of_files = len([name for name in os.listdir("2D/0/") if os.path.isfile(os.path.join("2D/0/", name))])
    data_array = np.matrix(np.loadtxt(open("2D/0/"+filename, "rb"), delimiter=";", usecols=range(640)))
    data_matrix += data_array/number_of_files


fig, ax = plt.subplots()
im = ax.imshow(data_matrix, cmap="jet")
fig.colorbar(im, ax=ax, label='Interactive colorbar')

plt.show()