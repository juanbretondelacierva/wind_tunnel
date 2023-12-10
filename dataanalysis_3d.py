import numpy as np
import matplotlib.pyplot as plt
import pickle
from matplotlib import cm
import scipy as sp

# Import data form pickle
with open('saved_variables_3d.pkl', 'rb') as file:
    data = pickle.load(file)


# min2d is filled with all the minimum values of each row of the convoluted data for each aoa
# so [[46]*500]
n = 8
filtersigmoid = np.concatenate((- np.ones(n), np.ones(n)))
min2d = []
for index in range(len(data['0'])):
    minimums = []
    for (aoa, matrix) in zip(data.keys(), data.values()):
        convolved_row = np.convolve(matrix[index], filtersigmoid, mode='valid')
        minindex = np.argmin(convolved_row)
        minimums.append(minindex)
    
    min2d.append(list(minimums))


smoothness_verical = 1 # mixes angles of attack (better not do) over 46 total
smoothness_horizontal = 21 # over 440 total

smoothingfilter_vertical = [np.array(np.ones(smoothness_verical)/smoothness_verical)]
smoothingfilter_horizontal = [[1/smoothness_horizontal]]*smoothness_horizontal

min2d = sp.signal.convolve2d(min2d, smoothingfilter_vertical, mode = 'same')
min2d = sp.signal.convolve2d(min2d, smoothingfilter_horizontal, mode = 'same')

fig, ax = plt.subplots()
ax.invert_yaxis()
for aoa in np.arange(46):
    if aoa <= 6 or aoa >= 20:
        continue
    aoalist = [min2d[i][aoa] for i in np.arange(len(data['0']))]
    ax.plot(aoalist, np.arange(len(data['0'])))
    if aoa == 15:
        break

ax.axvline(250, color = 'r', linestyle = '--')
ax.set_ylim(480 - smoothness_horizontal/2, smoothness_horizontal/2)
ax.axis('equal')

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
X, Y = np.meshgrid(np.arange(46), np.arange(len(data['0'])))
surf = ax.plot_surface(X, Y, np.array(min2d, dtype=int), cmap=cm.coolwarm,
                       linewidth=0)

# Plot settings
numplots = 46
columnsplot = 8
rowsplots = numplots//columnsplot +1

# First normal data plot
fig, ax = plt.subplots(rowsplots, columnsplot, sharex=True, sharey=True)

for i, (key, value) in enumerate(zip(data.keys(), data.values())):
    ax[i//columnsplot][i%columnsplot].set_title(f"{key}")
    im = ax[i//columnsplot][i%columnsplot].imshow(value, cmap='jet', vmin = 10.5, vmax = 12.1)

# Second (filtered) plot

# g0d filters: [ -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1]
# Filters should add to 0 in not --> change vmin, vmax in bottom plot
#n = 8
#filterconv = np.concatenate((- np.ones(n), np.ones(n)))
filtersigmoid = [(2/(1+np.exp(-x))-1) for x in np.arange(-5, 5.5, 0.5)]

saturation = 1 #Actually inverse but who cares, the lower the more saturated
fig, ax = plt.subplots(rowsplots, columnsplot, sharex=True, sharey=True)

for i, (key, value) in enumerate(zip(data.keys(), data.values())):
    convolved_data = np.array([np.convolve(row, filtersigmoid, mode='valid') for row in value])
    ax[i//columnsplot][i%columnsplot].set_title(f"{key}")
    im = ax[i//columnsplot][i%columnsplot].imshow(convolved_data, cmap='jet', vmin = -saturation, vmax = saturation)
    #fig.colorbar(im, ax=ax)

plt.show()