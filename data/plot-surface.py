#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def ss(x, R):
    return np.where(x < 2*R, 2*np.pi*R**2/x, 0)

def sv(x, R):
    return np.where(x < 2*R, np.pi*R*x + 2*np.pi*R**2, 4*np.pi*R**2)

ssc = np.load('ball-ss.npy')
svc = np.load('ball-sv.npy')

xs = np.linspace(0, 0.5, ssc.size)
plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 25)
plt.plot(xs, ssc)
plt.plot(xs, ss(xs, 0.2))
plt.ylim([0, 20])
plt.xlabel(r'$r$')
plt.ylabel(r'$F_{ssv}(r, 0.5)$')
plt.legend(['Calculation', 'Theory'])
plt.ticklabel_format(axis = "y", scilimits = (0, 0), useMathText = True)
plt.ticklabel_format(axis = "x", scilimits = (0, 0), useMathText = True)
plt.savefig('../images/ball-ssv.png')

xs = np.linspace(0, 0.5, svc.size)
plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 25)
plt.plot(xs, svc)
plt.plot(xs, sv(xs, 0.2))
plt.xlabel(r'$r$')
plt.ylabel(r'$F_{svv}(r, 0.5)$')
plt.legend(['Calculation', 'Theory'])
plt.ticklabel_format(axis = "y", scilimits = (0, 0), useMathText = True)
plt.ticklabel_format(axis = "x", scilimits = (0, 0), useMathText = True)
plt.savefig('../images/ball-svv.png')
