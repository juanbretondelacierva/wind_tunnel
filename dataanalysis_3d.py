import numpy as np
import os
import copy
import matplotlib.pyplot as plt
import pickle

def flatten_list(nested):
    flattened = []
    for item in nested:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened


with open('saved_variables_3d.pkl', 'rb') as file:
    data = pickle.load(file)

print(type(data['0']))

for key, value in zip(data.keys(), data.values()):
    fig, ax = plt.subplots()
    fig.suptitle(f"Angle of Attack {key}")
    im = ax.imshow(value, cmap='jet')
    fig.colorbar(im, ax=ax, label='Interactive colorbar')

    plt.show()