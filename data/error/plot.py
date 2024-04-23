#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def err(i, n, name):
    datal = np.load("lisp/data-%i-300-%s.npy" % (i, name))
    dataj = np.load("julia/data-%i-300-%s.npy" % (i, name))
    err = np.abs(datal - dataj) / datal
    err = err[n:, n:]
    return np.max(err)

def toangle(i):
    return np.pi/4 * i/10

xs = np.arange(1,10)
xs = toangle(xs)

errs3 = np.array(list(map(lambda i: err(i, 0, "s3"), range(1, 10))))
errsss = np.array(list(map(lambda i: err(i, 10, "surf3"), range(1, 10))))

plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 25)
ax1 = plt.gca()
ax2 = ax1.twinx()
p1, = ax1.plot(xs, errsss, 'b.-', label = r'$F_{sss}$')
p2, = ax2.plot(xs, errs3, 'r.-', label = r'$S_3$')
ax1.set_xlabel(r'$\phi$')
ax1.set_ylabel(r'$\max (\varepsilon)$, $F_{sss}$')
ax2.set_ylabel(r'$\max (\varepsilon)$, $S_3$')
ax1.ticklabel_format(axis = "y", scilimits = (0, 0), useMathText = True)
ax2.ticklabel_format(axis = "y", scilimits = (0, 0), useMathText = True)
ax1.legend(handles = [p1, p2])
plt.savefig('../../images/roterror-s3.png')
