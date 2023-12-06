import numpy as np
import os

data_matrix = np.zeros((480, 640))
data_matrix = np.asmatrix(data_matrix)
for filename in os.listdir("2D/0/"):
    number_of_files = len([name for name in os.listdir("2D/0/") if os.path.isfile(os.path.join("2D/0/", name))])
    data_array = np.matrix(np.loadtxt(open("2D/0/"+filename, "rb"), delimiter=";", usecols=range(640)))
    data_matrix += data_array/number_of_files

    print(data_matrix)