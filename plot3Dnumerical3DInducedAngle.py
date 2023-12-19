import matplotlib.pyplot as plt
import numpy as np
import colorsys
import os



#function that discretizes rainbow colours into a list depending on 
#the size of a dataset so that each plot can be distinguished according to it's height in the z axis
def generate_rainbow_colors(num_colors):
    colors = []
    for i in range(num_colors):
        hue = i / num_colors
        rgb = colorsys.hsv_to_rgb(hue, 1, 1)
        colors.append(tuple(float(c * 1) for c in rgb))
    return colors
#size of dataset
num_colors = 42
#list of colours
colours = generate_rainbow_colors(num_colors)

#function that converts csv files directly into a specific plot of 3D points, 
#having the data x and y, the value of z, the color, the marker style and the label as variables
def convertarrayandplot(data,z, c, label = ''):
    x, y = [item[0] for item in data], [item[1] for item in data]
    plt.plot(x, y, z, marker='.', label=label, color=c)
    return

#creates a plot figure
fig = plt.figure(figsize=(20,20))
#adds the z-axis in order to be a 3D plot
ax = fig.add_subplot(projection='3d')

#creates a list with all the z-values used as the angles of attack
zticks=[]
i=-2.5
while i<=18:
    zticks+=[i]
    i+=0.5

#function that gets every graph in order of the angle of attack 
#by reading the title of the files in the folder NumericalInducedAngle3D
#and does a 2D plot for the x,y data

def get_graph(order):
    for filename in os.listdir('.\\NumericalInducedAngle3D'):
        if str(filename)[0:-4]==order:
            data = np.loadtxt(open(os.path.join('.\\NumericalInducedAngle3D', filename), "rb"), delimiter=",", usecols=[0, 1],skiprows=1)
            convertarrayandplot(data,float(order),colours[zticks.index(float(order))],label= order)        
    return 0

#creates a 2D plot for every angle of attack 
#and locatesthem at their respective z values in the 3D plot
for i in zticks:
    get_graph(str(i))

#set title for the axis
ax.set_xlabel('Y-Span')
ax.set_ylabel('X-Induced Angle [deg]')
ax.set_zlabel('Z-Angle of Attack')

plt.show()