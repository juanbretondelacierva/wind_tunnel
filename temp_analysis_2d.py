import numpy as np
import os
from matplotlib import pyplot as plt

#aoa = ["-3","-2","-1","0","1","2","3","3.5","4","4.5","5","5.5","6","6.5","7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12","12.5","13","13.5","14","14.5","15","15.5","16","16.5","17","17.5","18","17.5h","17h","16.5h","16h","15.5h","15h","14.5h","14h","13.5h","13h","12.5h","12h","11.5h"]
aoa = ["2"]

right_limit = 446
left_limit = 196

def average_columns(array):
    return np.mean(array, axis=0)
    

def pixelate_columns(array):
    pixelated_row = np.zeros(50)
    for i in range(50):
        pixelated_row[i] = np.mean(array[:, 5*i : 5*i + 5])
    return pixelated_row


def row_to_image(array):
    image = np.asmatrix(np.zeros((int(50), int(50))))
    for i in range(int((right_limit-left_limit)/5)):
        image[i] = array
    return image

def derivate_row(array):
    return np.append(np.diff(array), np.mean(np.diff(array)))

def find_line(array):
    pixelated_row = np.zeros(50)
    index = np.argmax(np.abs(array))
    pixelated_row[index]=1
    return pixelated_row

def plot():
    for folder in aoa:
        data_matrix = np.asmatrix(np.zeros((right_limit-left_limit, right_limit-left_limit)))
        for filename in os.listdir("2D/"+str(folder)+"/"):
            number_of_files = len([name for name in os.listdir("2D/"+str(folder)+"/") if os.path.isfile(os.path.join("2D/"+str(folder)+"/", name))])
            data_array = np.matrix(np.loadtxt(open("2D/"+str(folder)+"/"+filename, "rb"), delimiter=";", usecols=range(left_limit, right_limit), skiprows=140, max_rows=(right_limit-left_limit)))
            data_matrix += data_array/number_of_files
        
        fig, ax = plt.subplots(1,2)
        fig.suptitle(f"Angle of Attack "+str(folder))
        im = ax[0].imshow(data_matrix, cmap="jet")
        fig.colorbar(im, ax=ax, label='Interactive colorbar')
        #im = ax[1].imshow(row_to_image(derivate_row(pixelate_columns(average_columns(data_matrix)))), cmap="jet")
        #fig.colorbar(im, ax=ax, label='Interactive colorbar')
        im = ax[1].imshow(row_to_image(find_line(derivate_row(pixelate_columns(average_columns(data_matrix))))), cmap="binary")
        fig.colorbar(im, ax=ax, label='Interactive colorbar')
        plt.show()
    

plot()