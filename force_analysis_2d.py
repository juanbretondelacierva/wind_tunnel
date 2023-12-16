import numpy as np
import os
from matplotlib import pyplot as plt

def cl_alpha():
    data_array = np.loadtxt(open("Forces/2D/corr_test.txt", "rb"), delimiter="	", usecols=[1,3], skiprows=2)
    alpha = data_array[:, 0]
    cl = data_array[:, 1]

    fig, ax = plt.subplots()
    ax.plot(alpha, cl, "o", color="blue", markersize=4)
    ax.plot(alpha, cl, "-", color="blue", label="Corrected $C_{L}$-$α$")

    data_array = np.loadtxt(open("Forces/2D/press_test.txt", "rb"), delimiter="	", usecols=[1,3], skiprows=2)
    alpha = data_array[:, 0]
    cl = data_array[:, 1]

    ax.plot(alpha, cl, "o", color="orange", markersize=4)
    ax.plot(alpha, cl, "-", color="orange", label="Uncorrected $C_{L}$-$α$")

    ax.set_xlabel('$α$ (deg)')
    ax.set_ylabel('$C_{L}$ (-)')
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
    ax.plot(alpha, cm, "-", color="blue", label="Corrected $C_{m}$-$α$")

    data_array = np.loadtxt(open("Forces/2D/press_test.txt", "rb"), delimiter="	", usecols=[1,4], skiprows=2)
    alpha = data_array[:, 0]
    cm = data_array[:, 1]

    ax.plot(alpha, cm, "o", color="orange", markersize=4)
    ax.plot(alpha, cm, "-", color="orange", label="Uncorrected $C_{m}$-$α$")

    ax.set_xlabel('$α$ (deg)')
    ax.set_ylabel('$C_{m}$ (-)')

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
    ax.plot(alpha, cd, "-", color="blue", label="Corrected $C_{D}$-$α$")

    data_array = np.loadtxt(open("Forces/2D/press_test.txt", "rb"), delimiter="	", usecols=[1,2], skiprows=2)
    alpha = data_array[:, 0]
    cd = data_array[:, 1]

    ax.plot(alpha, cd, "o", color="orange", markersize=4)
    ax.plot(alpha, cd, "-", color="orange", label="Uncorrected $C_{D}$-$α$")

    ax.set_xlabel('$α$ (deg)')
    ax.set_ylabel('$C_{D}$ (-)')

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
    ax.plot(cd, cl, "-", color="blue", label="Corrected $C_{L}$-$C_{D}$")

    data_array = np.loadtxt(open("Forces/2D/press_test.txt", "rb"), delimiter="	", usecols=[2,3], skiprows=2)
    cd = data_array[:, 0]
    cl = data_array[:, 1]

    ax.plot(cd, cl, "o", color="orange", markersize=4)
    ax.plot(cd, cl, "-", color="orange", label="Uncorrected $C_{L}$-$C_{D}$")

    ax.set_xlabel('$C_{D}$ (-)')
    ax.set_ylabel('$C_{L}$ (-)')

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
                    ax.plot(x, cp, "-", color="blue", label=("$C_{D}$ - $α$°"))
                else:
                    ax.plot(x, cp, "-", color="orange", label=("$C_{D}$ - $α$° H"))


    ax.set_xlabel('$C_{D}$ (-)')
    ax.set_ylabel('X (m)')

    ax.set_xticks(np.arange(-3, 19, 2))
    plt.grid()
    plt.legend(ncol=5)
    plt.show()

cl_alpha()
cd_alpha()
cl_cd()
cm_alpha()