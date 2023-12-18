import matplotlib.pyplot as plt
import numpy as np
import colorsys
import os


def convertarrayandplot(data,z, label = ''):
    x, y = [item[0] for item in data], [item[1] for item in data]
    plt.plot(x, y, z, marker='.', label=label)
    return

def generate_rainbow_colors(num_colors):
    colors = []
    for i in range(num_colors):
        hue = i / num_colors
        rgb = colorsys.hsv_to_rgb(hue, 1, 1)
        colors.append(tuple(int(c * 255) for c in rgb))
    return colors

num_colors = 42
colours = generate_rainbow_colors(num_colors)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
zticks=[]
i=-2.5
while i<=18:
    zticks+=[i]
    i+=0.5

def get_graph(order):
    for filename in os.listdir('.\\NumericalTransition3D'):
        if str(filename)[0:-4]==order:
            data = np.loadtxt(open(os.path.join('.\\NumericalTransition3D', filename), "rb"), delimiter=",", usecols=[0, 1],skiprows=1)
            convertarrayandplot(data,float(order),label= order)
    return 0


for i in zticks:
    get_graph(str(i))

ax.set_zticks(zticks)
plt.show()
