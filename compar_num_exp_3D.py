import numpy as np
import os
from matplotlib import pyplot as plt 


def cl_cd():
    data_array = np.loadtxt(open("Forces/3D/corr_test.txt", "rb"), delimiter="	", usecols=[4,3], skiprows=2)
    cd = data_array[:, 0]
    cl = data_array[:, 1]

    fig, ax = plt.subplots()
    ax.plot(cd, cl, "-o", color="blue", markersize=4, markeredgecolor='black', label="Experiment ")


    data_LTT = np.loadtxt(open(os.path.join('.\\Numerical3D', "CD-CL 3D.csv"), "rb"), delimiter=",", usecols=[0, 1], skiprows=1, max_rows=42)   
    convertarrayandplot(data_LTT, "-",".", label = 'Simulation')

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
    ax.plot(alpha, cm, "-o", color="blue", markersize=4, markeredgecolor='black', label="Experiment ")
    #ax.plot(alpha, cm, "o", color="blue", markersize=4)
    #ax.plot(alpha, cm, "-", color="blue", label="Corrected Cl-Cd")

    data_LTT = np.loadtxt(open(os.path.join('.\\Numerical3D', "Cm-Alpha 3D.csv"), "rb"), delimiter=",", usecols=[0, 1], skiprows=1, max_rows=42)   
    convertarrayandplot(data_LTT, "-",".", label = 'Simulation')
    

    ax.set_xlabel('$α$ (deg)')
    ax.set_ylabel('$C_M$')
    plt.grid()
    plt.legend()
    plt.show()

def convertarrayandplot(data, trace, dot, label = ''):
    x, y = [item[0] for item in data], [item[1] for item in data]
    plt.plot(x, y, linestyle=trace ,marker=dot, color='orange', markeredgecolor='black', label=label)
    return

def cl_alpha():
    data_array = np.loadtxt(open("Forces/3D/corr_test.txt", "rb"), delimiter="	", usecols=[1,3], skiprows=2)
    alpha = data_array[:, 0]
    cl = data_array[:, 1]

    fig, ax = plt.subplots()
    ax.plot(alpha, cl, "-o", color="blue", markersize=4, markeredgecolor='black', label="Experiment ")

    data_LTT = np.loadtxt(open(os.path.join('.\\Numerical3D', "CL-Alpha 3D.csv"), "rb"), delimiter=",", usecols=[0, 1], skiprows=1, max_rows=42)   
    convertarrayandplot(data_LTT, "-",".", label = 'Simulation')

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
    ax.plot(alpha, cd, "-o", color="blue", markersize=4, markeredgecolor='black', label="Experiment ")

    data_LTT = np.loadtxt(open(os.path.join('.\\Numerical3D', "CD-Alpha.csv"), "rb"), delimiter=",", usecols=[0, 1], skiprows=1, max_rows=42)
    convertarrayandplot(data_LTT, "-",".",  label = 'Simulation')

    ax.set_xlabel('$α$ (deg)')
    ax.set_ylabel('$C_D$ (-)')
    ax.set_xticks(np.arange(-3, 18, 1))
    
    plt.grid()
    plt.legend()
    plt.show()

    
cl_alpha()
cl_cd()
cm_alfa()
cd_alpha()
