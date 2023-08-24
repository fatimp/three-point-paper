#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def s2_th(x, λ, R):
    ρ = 4/3*np.pi*λ*R**3
    return np.exp(-ρ * np.where(x < 2*R, 1 + 3/4*x/R - 1/16*(x/R)**3, 2))

s2 = np.load('test-s2.npy')
xs = np.linspace(0, 0.5, s2.size)

plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 25)
plt.plot(xs, s2)
plt.plot(xs, s2_th(xs, 5000, 0.02))
plt.xlabel(r'$r$')
plt.ylabel(r'$S_3(0, r)$')
plt.ticklabel_format(axis = "y", scilimits = (0, 0), useMathText = True)
plt.ticklabel_format(axis = "x", scilimits = (0, 0), useMathText = True)
plt.legend(['Calculation', 'Theory'])
plt.savefig('../images/balls-s3.png')

plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 30)
plt.plot(xs, s2)
plt.plot(xs, s2_th(xs, 5000, 0.02))
plt.ticklabel_format(axis = "y", scilimits = (0, 0), useMathText = True)
plt.ticklabel_format(axis = "x", scilimits = (0, 0), useMathText = True)
plt.xlim([0.03, 0.06])
plt.ylim([0.71, 0.73])
plt.savefig('../images/balls-s3-zoom.png')
