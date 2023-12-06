import numpy as np
data_array = np.loadtxt(open("2D/0/1sigma_2023-12-01_09-22-11.csv", "rb"), delimiter=";", usecols=range(640))
print(data_array[1][0])