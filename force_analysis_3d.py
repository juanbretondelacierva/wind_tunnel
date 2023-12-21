
import numpy as np
import os
from matplotlib import pyplot as plt

def cl_alpha():
    data_array = np.loadtxt(open("Forces/3D/corr_test.txt", "rb"), delimiter="	", usecols=[1,3], skiprows=2)
    alpha = data_array[:, 0]
    cl = data_array[:, 1]

    fig, ax = plt.subplots()
    ax.plot(alpha, cl, "-^", color="blue", markersize=6, markeredgecolor='black', label="Corrected $C_{L}$-$α$")

    data_array = np.loadtxt(open("Forces/3D/unc_test.txt", "rb"), delimiter="	", usecols=[1,3], skiprows=2)
    alpha = data_array[:, 0]
    cl = data_array[:, 1]

    ax.plot(alpha, cl, "-o", color="orange", markersize=4, markeredgecolor='black', label="Uncorrected $C_{L}$-$α$")

    ax.set_xlabel('$α$ (deg)')
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
    ax.plot(alpha, cd, "o", color="blue", markersize=4)
    ax.plot(alpha, cd, "-", color="blue", label="Corrected $C_D$-$α$")

    data_array = np.loadtxt(open("Forces/3D/unc_test.txt", "rb"), delimiter="	", usecols=[1,4], skiprows=2)
    alpha = data_array[:, 0]
    cd = data_array[:, 1]

    ax.plot(alpha, cd, "o", color="orange", markersize=4)
    ax.plot(alpha, cd, "-", color="orange", label="Uncorrected $C_D$-$α$")

    ax.set_xlabel('$α$ (deg)')
    ax.set_ylabel('$C_D$ (-)')
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
    ax.plot(cd, cl, "-", color="blue", label="Corrected $C_L$-$C_D$")

    data_array = np.loadtxt(open("Forces/3D/unc_test.txt", "rb"), delimiter="	", usecols=[4,3], skiprows=2)
    cd = data_array[:, 0]
    cl = data_array[:, 1]

    ax.plot(cd, cl, "o", color="orange", markersize=4)
    ax.plot(cd, cl, "-", color="orange", label="Uncorrected $C_L$-$C_D$")

    ax.set_xlabel('$C_D$ (-)')
    ax.set_ylabel('$C_L$ (-)')
    plt.grid()
    plt.legend()
    plt.show()
    
def cm_alfa():
    data_array = np.loadtxt(open("Forces/3D/corr_test.txt", "rb"), delimiter="	", usecols=[1,6], skiprows=2)
    alpha = data_array[:, 0]
    cm = data_array[:, 1]

    fig, ax = plt.subplots()
    ax.plot(alpha, cm, "-^", color="blue", markersize=6, markeredgecolor='black', label="Corrected $C_{M_{0.25c}}$-$α$")
    #ax.plot(alpha, cm, "o", color="blue", markersize=4)
    #ax.plot(alpha, cm, "-", color="blue", label="Corrected Cl-Cd")

    data_array = np.loadtxt(open("Forces/3D/unc_test.txt", "rb"), delimiter="	", usecols=[1,11], skiprows=2)
    alpha = data_array[:, 0]
    cm = data_array[:, 1]

    ax.plot(alpha, cm, "-o", color="orange", markersize=4, markeredgecolor='black', label="Uncorrected $C_{M}$-$α$")
    

    ax.set_xlabel('$α$ (deg)')
    ax.set_ylabel('$C_M$')
    plt.grid()
    plt.legend()
    plt.show()

cl_alpha()
cd_alpha()
cl_cd()
cm_alfa()
