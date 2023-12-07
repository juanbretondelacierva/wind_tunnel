import numpy as np
import matplotlib.pyplot as plt
import pickle

# Import data form pickle
with open('saved_variables_3d.pkl', 'rb') as file:
    data = pickle.load(file)


# Plot settings
numplots = 46
columnsplot = 12
rowsplots = numplots//columnsplot +1

# First normal data plot
fig, ax = plt.subplots(rowsplots, columnsplot, sharex=True, sharey=True)

for i, (key, value) in enumerate(zip(data.keys(), data.values())):
    ax[i//columnsplot][i%columnsplot].set_title(f"{key}")
    im = ax[i//columnsplot][i%columnsplot].imshow(value, cmap='jet', vmin = 10.5, vmax = 12.5)

plt.show()

# Second (filtered) plot

# g0d filters: [ -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1]
# Filters should add to 0 in not --> change vmin, vmax in bottom plot
filterconv = [ -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1]

saturation = 1 #Actually inverse but who cares, the lower the more saturated
fig, ax = plt.subplots(rowsplots, columnsplot, sharex=True, sharey=True)

for i, (key, value) in enumerate(zip(data.keys(), data.values())):
    convolved_data = np.array([np.convolve(row, filterconv, mode='valid') for row in value])
    ax[i//columnsplot][i%columnsplot].set_title(f"{key}")
    im = ax[i//columnsplot][i%columnsplot].imshow(convolved_data, cmap='jet', vmin = -saturation, vmax = saturation)
    #fig.colorbar(im, ax=ax)

plt.show()