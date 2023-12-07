import numpy as np
import matplotlib.pyplot as plt
import pickle

with open('saved_variables_3d.pkl', 'rb') as file:
    data = pickle.load(file)


filterconv = [ -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1]

columnsplot = 16
fig, ax = plt.subplots(3, columnsplot)

for i, (key, value) in enumerate(zip(data.keys(), data.values())):
    ax[i//columnsplot][i%columnsplot].set_title(f"{key}")
    im = ax[i//columnsplot][i%columnsplot].imshow(value, cmap='jet')

plt.show()

fig, ax = plt.subplots(3, columnsplot)
for i, (key, value) in enumerate(zip(data.keys(), data.values())):
    convolved_data = np.array([np.convolve(row, filterconv, mode='valid') for row in value])
    ax[i//columnsplot][i%columnsplot].set_title(f"{key}")
    im = ax[i//columnsplot][i%columnsplot].imshow(convolved_data, cmap='jet')
    #fig.colorbar(im, ax=ax)

plt.show()