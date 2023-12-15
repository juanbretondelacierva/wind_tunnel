
import numpy as np
import os
from matplotlib import pyplot as plt

def cl_alpha():
    data_array = np.loadtxt(open("Forces/3D/corr_test.txt", "rb"), delimiter="	", usecols=[1,3], skiprows=2)
    alpha = data_array[:, 0]
    cl = data_array[:, 1]

    fig, ax = plt.subplots()
    ax.plot(alpha, cl, "o", color="blue", markersize=4)
    ax.plot(alpha, cl, "-", color="blue", label="Corrected Cl-alpha")

    data_array = np.loadtxt(open("Forces/3D/unc_test.txt", "rb"), delimiter="	", usecols=[1,3], skiprows=2)
    alpha = data_array[:, 0]
    cl = data_array[:, 1]

    #ax.plot(alpha, cl, "o", color="orange", markersize=4)
    #ax.plot(alpha, cl, "-", color="orange", label="Uncorrected Cl-alpha")

    ax.set_xlabel('Alpha(°)')
    ax.set_ylabel('Cl')
    ax.set_xticks(np.arange(-3, 19, 1))

    plt.grid()
    plt.legend()
    plt.show()

def cd_alpha():
    data_array = np.loadtxt(open("Forces/3D/corr_test.txt", "rb"), delimiter="	", usecols=[1,4], skiprows=2)
    alpha = data_array[:, 0]
    cd = data_array[:, 1]

    fig, ax = plt.subplots()
    ax.plot(alpha, cd, "o", color="blue", markersize=4)
    ax.plot(alpha, cd, "-", color="blue", label="Corrected Cd-alpha")

    data_array = np.loadtxt(open("Forces/3D/unc_test.txt", "rb"), delimiter="	", usecols=[1,4], skiprows=2)
    alpha = data_array[:, 0]
    cd = data_array[:, 1]

    ax.plot(alpha, cd, "o", color="orange", markersize=4)
    ax.plot(alpha, cd, "-", color="orange", label="Uncorrected Cd-alpha")

    ax.set_xlabel('Alpha')
    ax.set_ylabel('Cd')
    ax.set_xticks(np.arange(-3, 18, 1))
    
    plt.grid()
    plt.legend()
    plt.show()

def cl_cd():
    data_array = np.loadtxt(open("Forces/3D/corr_test.txt", "rb"), delimiter="	", usecols=[4,3], skiprows=2)
    cd = data_array[:, 0]
    cl = data_array[:, 1]

    fig, ax = plt.subplots()
    ax.plot(cd, cl, "o", color="blue", markersize=4)
    ax.plot(cd, cl, "-", color="blue", label="Corrected Cl-Cd")

    data_array = np.loadtxt(open("Forces/3D/unc_test.txt", "rb"), delimiter="	", usecols=[4,3], skiprows=2)
    cd = data_array[:, 0]
    cl = data_array[:, 1]

    ax.plot(cd, cl, "o", color="orange", markersize=4)
    ax.plot(cd, cl, "-", color="orange", label="Uncorrected Cl-Cd")

    ax.set_xlabel('Cd')
    ax.set_ylabel('Cl')
    plt.grid()
    plt.legend()
    plt.show()

cl_alpha()