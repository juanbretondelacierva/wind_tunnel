
import numpy as np
import os
from matplotlib import pyplot as plt

def cl_alpha():
    data_array = np.loadtxt(open("Forces/3D/corr_test.txt", "rb"), delimiter="	", usecols=[1,3], skiprows=2)
    alpha = data_array[:, 0]
    cl = data_array[:, 1]

    fig, ax = plt.subplots()
    ax.plot(alpha, cl, "-^", color="blue", markersize=4, markeredgecolor='blue', label="$C_{L}$ - \u03B1 wing")

    data_array = np.loadtxt(open("Forces/2D/corr_test.txt", "rb"), delimiter="	", usecols=[1,3], skiprows=2)
    alpha = data_array[:, 0]
    cl = data_array[:, 1]

    ax.plot(alpha, cl, "-o", color="orange", markersize=4, markeredgecolor='orange', label="$C_{l}$ - \u03B1 airfoil")

    ax.set_xlabel('\u03B1 (deg)')
    ax.set_ylabel('$C_{L}$ (-)')
    ax.set_xticks(np.arange(-3, 19, 2))

    plt.grid()
    plt.legend()
    plt.show()

def cd_alpha():
    data_array = np.loadtxt(open("Forces/3D/corr_test.txt", "rb"), delimiter="	", usecols=[1,4], skiprows=2)
    alpha = data_array[:, 0]
    cd = data_array[:, 1]

    fig, ax = plt.subplots()
    ax.plot(alpha, cd, "^", color="blue", markersize=4)
    ax.plot(alpha, cd, "-", color="blue", label="$C_{D}$ - \u03B1 wing")

    data_array = np.loadtxt(open("Forces/2D/corr_test.txt", "rb"), delimiter="	", usecols=[1,2], skiprows=2)
    alpha = data_array[:, 0]
    cd = data_array[:, 1]

    ax.plot(alpha, cd, "o", color="orange", markersize=4)
    ax.plot(alpha, cd, "-", color="orange", label="$C_{d}$ - \u03B1 airfoil")

    ax.set_xlabel('\u03B1 (deg)')
    ax.set_ylabel('$C_{D}$ (-)')
    ax.set_xticks(np.arange(-3, 18, 1))
    
    plt.grid()
    plt.legend()
    plt.show()

def cl_cd():
    data_array = np.loadtxt(open("Forces/3D/corr_test.txt", "rb"), delimiter="	", usecols=[4,3], skiprows=2)
    cd = data_array[:, 0]
    cl = data_array[:, 1]

    fig, ax = plt.subplots()
    ax.plot(cd, cl, "^", color="blue", markersize=4)
    ax.plot(cd, cl, "-", color="blue", label="$C_{L}$ - $C_{D}$ wing")

    data_array = np.loadtxt(open("Forces/2D/corr_test.txt", "rb"), delimiter="	", usecols=[2,3], skiprows=2)
    cd = data_array[:, 0]
    cl = data_array[:, 1]

    ax.plot(cd, cl, "o", color="orange", markersize=4)
    ax.plot(cd, cl, "-", color="orange", label="$C_{l}$ - $C_{d}$ airfoil")

    ax.set_xlabel('$C_{D} (-)$')
    ax.set_ylabel('$C_{L} (-)$')
    plt.grid()
    plt.legend()
    plt.show()

def cm_alfa():
    data_array = np.loadtxt(open("Forces/3D/corr_test.txt", "rb"), delimiter="	", usecols=[1,11], skiprows=2)
    cd = data_array[:, 0]
    cl = data_array[:, 1]

    fig, ax = plt.subplots()
    ax.plot(cd, cl, "^", color="blue", markersize=4)
    ax.plot(cd, cl, "-", color="blue", label="$C_{M}$ - \u03B1 wing")

    data_array = np.loadtxt(open("Forces/2D/corr_test.txt", "rb"), delimiter="	", usecols=[1,4], skiprows=2)
    cd = data_array[:, 0]
    cl = data_array[:, 1]

    ax.plot(cd, cl, "o", color="orange", markersize=4)
    ax.plot(cd, cl, "-", color="orange", label="$C_{m}$ - \u03B1 airfoil")

    ax.set_xlabel('$\u03B1$ (deg)')
    ax.set_ylabel('$C_{M} (-)$')
    plt.grid()
    plt.legend()
    plt.show()



cl_alpha()
cd_alpha()
cl_cd()
cm_alfa()