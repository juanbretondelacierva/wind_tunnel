import numpy as np
import os
from matplotlib import pyplot as plt

aoa = ["-3","-2","-1","0","1","2","3","3.5","4","4.5","5","5.5","6","6.5","7","7.5","8","8.5","9","9.5","10","10.5","11","11.5","12","12.5","13","13.5","14","14.5","15","15.5","16","16.5","17","17.5","18","17.5h","17h","16.5h","16h","15.5h","15h","14.5h","14h","13.5h","13h","12.5h","12h","11.5h"]
#aoa = ["6"]

right_limit = 446
left_limit = 196
aoa_plot = []
chordpos = np.array([])
i = 0

def average_columns(array):
    return np.mean(array, axis=0)
    

def pixelate_columns(array):
    pixelated_row = np.zeros(50)
    for i in range(50):
        pixelated_row[i] = np.mean(array[:,5*i : 5*i + 5])
    return pixelated_row


def row_to_image(array):
    image = np.asmatrix(np.zeros((int(8), int(50))))
    for i in range(int(8)):
        image[i] = array
    return image

def derivate_row(array):
    return np.append(np.diff(array), np.mean(np.diff(array)))

def find_line(array, id):
    global chordpos, aoa_plot
    pixelated_row = np.zeros(50)
    if id >= 18:
        index = np.argmax(np.abs(array))
    else:
        index = np.argmax(array)
    pixelated_row[index]=1
    aoa_value = float(aoa[i].replace("h", ""))
    aoa_plot.append(aoa_value)
    chordpos = np.append(chordpos, index/50*240)
    return pixelated_row

def plot():
    global i, aoa_plot
    aoa_plot = [] 
    for folder in aoa:
        folder_path = os.path.join("2D", str(folder))
        data_matrix = np.asmatrix(np.zeros((40, right_limit - left_limit)))
        for filename in os.listdir(folder_path):
            number_of_files = len([name for name in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, name))])
            data_array = np.matrix(np.loadtxt(open(os.path.join(folder_path, filename), "rb"), delimiter=";", usecols=range(left_limit, right_limit), skiprows=300, max_rows=40))
            data_matrix += data_array / number_of_files

        if i >= 3:
            fig, ax = plt.subplots(2,2)
            print("Angle of Attack "+str(folder))
            im = ax[0][0].imshow(data_matrix, cmap="jet")
            ax[0][0].set_title("Original")
            fig.colorbar(im, ax=ax, label="Original images' colorbar")
            im = ax[0][1].imshow(row_to_image(pixelate_columns(average_columns(data_matrix))), cmap="jet")
            ax[0][1].set_title("Mean columns")
            fig.colorbar(im, ax=ax, label="Mean columns' colorbar")
            im = ax[1][1].imshow(row_to_image(derivate_row(pixelate_columns(average_columns(data_matrix)))), cmap="jet")
            ax[1][1].set_title("Derivative")
            fig.colorbar(im, ax=ax, label="Derivative's colorbar")
            im = ax[1][0].imshow(row_to_image(find_line(derivate_row(pixelate_columns(average_columns(data_matrix))), i)), cmap="binary")
            ax[1][0].set_title("Transition location")
            plt.show()
        else:
            find_line(derivate_row(pixelate_columns(average_columns(data_matrix))), i)
        i += 1
    fig, ax = plt.subplots()
    ax.plot(aoa, chordpos, "-o", color="orange", markersize="5", markeredgecolor="black")
    ax.set_xlabel("α (deg)")
    ax.set_ylabel("Trailing edge distance (mm)")
    ax.set_xticks(np.arange(-3, 50, 3))
    plt.grid()
    plt.show()
    

plot()