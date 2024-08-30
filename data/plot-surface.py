#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def ss(x, R):
    return np.where(x < 2*R, 2*np.pi*R**2/x, 0)

def sv(x, R):
    return np.where(x < 2*R, np.pi*R*x + 2*np.pi*R**2, 4*np.pi*R**2)

ssc = np.load('ball-ss.npy')
svc = np.load('ball-sv.npy')

xs1 = np.linspace(0, 0.5, svc.size)
xs2 = np.linspace(0, 0.5, 1000)
plt.figure(figsize = (10, 9), dpi = 300)
plt.rc('font', size = 25)
plt.plot(xs1, ssc, color = '#1f77b4', linewidth = 3)
plt.plot(xs2, ss(xs2, 0.2), color = '#ff7f0e', linestyle = '-.', linewidth = 3)
plt.ylim([0, 20])
plt.xlabel(r'$r$')
plt.ylabel(r'$F_{ssv}(r, 0.5)$')
plt.legend(['Calculation', 'Theory'])
plt.ticklabel_format(axis = "y", scilimits = (0, 0), useMathText = True)
plt.ticklabel_format(axis = "x", scilimits = (0, 0), useMathText = True)
plt.savefig('../images/ball-ssv.png')

xs1 = np.linspace(0, 0.5, svc.size)
xs2 = np.linspace(0, 0.5, 1000)
plt.figure(figsize = (10, 9), dpi = 300)
plt.rc('font', size = 25)
plt.plot(xs1, svc, color = '#1f77b4', linewidth = 3)
plt.plot(xs2, sv(xs2, 0.2), color = '#ff7f0e', linestyle = '-.', linewidth = 3)
plt.xlabel(r'$r$')
plt.ylabel(r'$F_{svv}(r, 0.5)$')
plt.legend(['Calculation', 'Theory'])
plt.ticklabel_format(axis = "y", scilimits = (0, 0), useMathText = True)
plt.ticklabel_format(axis = "x", scilimits = (0, 0), useMathText = True)
plt.savefig('../images/ball-svv.png')
