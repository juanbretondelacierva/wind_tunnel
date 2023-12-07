import numpy as np
import os
import copy
import matplotlib.pyplot as plt
import pickle
import 3ddataloading

filterconv = [-1, -1, -1, -1, -1, 1, 1, 1, 1, 1]
print(data['0'])
convolved_result = np.array([np.convolve(row, filterconv) for row in data['0']])
print(convolved_result)


for key, value in zip(data.keys(), data.values()):
    fig, ax = plt.subplots()
    fig.suptitle(f"Angle of Attack {key}")
    im = ax.imshow(value, cmap='jet')
    fig.colorbar(im, ax=ax, label='Interactive colorbar')

    plt.show()