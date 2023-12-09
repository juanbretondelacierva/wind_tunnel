import numpy as np
import matplotlib.pyplot as plt
import pickle
from matplotlib import cm
import scipy as sp

# Import data form pickle
with open('saved_variables_3d.pkl', 'rb') as file:
    data = pickle.load(file)


def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='valid')
    return y_smooth

filterconv = [ -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1]
min2d = []
for index in range(len(data['0'])):
    minimums = []
    for (aoa, matrix) in zip(data.keys(), data.values()):
        convolved_row = np.convolve(matrix[index], filterconv, mode='valid')
        minindex = np.argmin(convolved_row)
        minimums.append(minindex)
    
    min2d.append(list(minimums))


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
X, Y = np.meshgrid(np.arange(46), np.arange(len(data['0'])))
min2d = sp.ndimage.uniform_filter(min2d, size = 6, mode = 'constant')
surf = ax.plot_surface(X, Y, np.array(min2d, dtype=int), cmap=cm.coolwarm,
                       linewidth=0)
plt.show()


# Plot settings
numplots = 46
columnsplot = 12
rowsplots = numplots//columnsplot +1

# First normal data plot
fig, ax = plt.subplots(rowsplots, columnsplot, sharex=True, sharey=True)

for i, (key, value) in enumerate(zip(data.keys(), data.values())):
    ax[i//columnsplot][i%columnsplot].set_title(f"{key}")
    im = ax[i//columnsplot][i%columnsplot].imshow(value, cmap='jet', vmin = 10.5, vmax = 12.5)

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

#plt.show()