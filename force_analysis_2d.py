import numpy as np
import os
from matplotlib import pyplot as plt

def cl_alpha():
    data_array = np.loadtxt(open("Forces/2D/corr_test.txt", "rb"), delimiter="	", usecols=[1,3], skiprows=2)
    alpha = data_array[:, 0]
    cl = data_array[:, 1]

    fig, ax = plt.subplots()
    ax.plot(alpha, cl, "o", color="blue", markersize=4)
    ax.plot(alpha, cl, "-", color="blue", label="Corrected Cl-alpha")

    data_array = np.loadtxt(open("Forces/2D/press_test.txt", "rb"), delimiter="	", usecols=[1,3], skiprows=2)
    alpha = data_array[:, 0]
    cl = data_array[:, 1]

    ax.plot(alpha, cl, "o", color="orange", markersize=4)
    ax.plot(alpha, cl, "-", color="orange", label="Uncorrected Cl-alpha")

    ax.set_xlabel('Alpha (°)')
    ax.set_ylabel('Cl (-)')
    ax.set_xticks(np.arange(-3, 19, 2))

    plt.grid()
    plt.legend()
    plt.show()

def cm_alpha():
    data_array = np.loadtxt(open("Forces/2D/corr_test.txt", "rb"), delimiter="	", usecols=[1,4], skiprows=2)
    alpha = data_array[:, 0]
    cm = data_array[:, 1]

    fig, ax = plt.subplots()
    ax.plot(alpha, cm, "o", color="blue", markersize=4)
    ax.plot(alpha, cm, "-", color="blue", label="Corrected Cm-alpha")

    data_array = np.loadtxt(open("Forces/2D/press_test.txt", "rb"), delimiter="	", usecols=[1,4], skiprows=2)
    alpha = data_array[:, 0]
    cm = data_array[:, 1]

    ax.plot(alpha, cm, "o", color="orange", markersize=4)
    ax.plot(alpha, cm, "-", color="orange", label="Uncorrected Cm-alpha")

    ax.set_xlabel('Alpha (°)')
    ax.set_ylabel('Cm (-)')

    ax.set_xticks(np.arange(-3, 19, 2))
    plt.grid()
    plt.legend()
    plt.show()

def cd_alpha():
    data_array = np.loadtxt(open("Forces/2D/corr_test.txt", "rb"), delimiter="	", usecols=[1,2], skiprows=2)
    alpha = data_array[:, 0]
    cd = data_array[:, 1]

    fig, ax = plt.subplots()
    ax.plot(alpha, cd, "o", color="blue", markersize=4)
    ax.plot(alpha, cd, "-", color="blue", label="Corrected Cd-alpha")

    data_array = np.loadtxt(open("Forces/2D/press_test.txt", "rb"), delimiter="	", usecols=[1,2], skiprows=2)
    alpha = data_array[:, 0]
    cd = data_array[:, 1]

    ax.plot(alpha, cd, "o", color="orange", markersize=4)
    ax.plot(alpha, cd, "-", color="orange", label="Uncorrected Cd-alpha")

    ax.set_xlabel('Alpha (°)')
    ax.set_ylabel('Cd (-)')

    ax.set_xticks(np.arange(-3, 19, 2))
    plt.grid()
    plt.legend()
    plt.show()

def cl_cd():
    data_array = np.loadtxt(open("Forces/2D/corr_test.txt", "rb"), delimiter="	", usecols=[2,3], skiprows=2)
    cd = data_array[:, 0]
    cl = data_array[:, 1]

    fig, ax = plt.subplots()
    ax.plot(cd, cl, "o", color="blue", markersize=4)
    ax.plot(cd, cl, "-", color="blue", label="Corrected Cl-Cd")

    data_array = np.loadtxt(open("Forces/2D/press_test.txt", "rb"), delimiter="	", usecols=[2,3], skiprows=2)
    cd = data_array[:, 0]
    cl = data_array[:, 1]

    ax.plot(cd, cl, "o", color="orange", markersize=4)
    ax.plot(cd, cl, "-", color="orange", label="Uncorrected Cl-Cd")

    ax.set_xlabel('Cd (-)')
    ax.set_ylabel('Cl (-)')

    ax.set_xticks(np.arange(0, 0.3, 0.05))
    plt.grid()
    plt.legend()
    plt.show()

def cp_dist():
    x = np.loadtxt(open("Forces/2D/cp_test.txt", "rb"), delimiter="	", usecols=0, skiprows=2)
    fig, ax = plt.subplots()
    for i in range(0, 53, 1):
        if i == 6 or i ==8:
            continue
        else:
            if i == 48 or i == 28:
                cp = np.loadtxt(open("Forces/2D/cp_test.txt", "rb"), delimiter="	", usecols=(i+1), skiprows=2)
                alpha = np.loadtxt(open("Forces/2D/cp_test.txt", "rb"), delimiter="	", usecols=(i+1), skiprows=1, max_rows=1)
                ax.plot(x, cp, "o", markersize=2)
                if i <= 38:
                    ax.plot(x, cp, "-", color="blue", label=("Cd - "+str(alpha)+"º"))
                else:
                    ax.plot(x, cp, "-", color="orange", label=("Cd - "+str(alpha)+"º H"))


    ax.set_xlabel('Cd (-)')
    ax.set_ylabel('X (m)')

    ax.set_xticks(np.arange(-3, 19, 2))
    plt.grid()
    plt.legend(ncol=5)
    plt.show()

cl_alpha()
cd_alpha()
cl_cd()
cm_alpha()