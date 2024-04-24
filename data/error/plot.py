#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def err(i, n, side, name):
    datal = np.load("lisp/data-%i-%i-%s.npy" % (i, side, name))
    dataj = np.load("julia/data-%i-%i-%s.npy" % (i, side, name))
    err = np.abs(datal - dataj) / datal
    err = err[n:, n:]
    return np.max(err)

def toangle(i):
    return np.pi/4 * i/10

xs = np.arange(1,10)
xs = toangle(xs)

errs3_300 = np.array(list(map(lambda i: err(i, 0, 300, "s3"), range(1, 10))))
errsss_300 = np.array(list(map(lambda i: err(i, 10, 300, "surf3"), range(1, 10))))
errs3_600 = np.array(list(map(lambda i: err(i, 0, 600, "s3"), range(1, 10))))
errsss_600 = np.array(list(map(lambda i: err(i, 10, 600, "surf3"), range(1, 10))))

#plt.figure(figsize = (10, 8), dpi = 300)
#plt.rc('font', size = 25)
ax1 = plt.gca()
ax2 = ax1.twinx()
p1, = ax1.plot(xs, errsss_300, 'b.-', label = r'$F_{sss}, 300 \times 300 \times 300$')
p2, = ax1.plot(xs, errsss_600, 'g.-', label = r'$F_{sss}, 600 \times 600 \times 600$')
p3, = ax2.plot(xs, errs3_300, 'r.-', label = r'$S_3, 300 \times 300 \times 300$')
p4, = ax2.plot(xs, errs3_600, 'm.-', label = r'$S_3, 600 \times 600 \times 600$')
ax1.set_xlabel(r'$\phi$')
ax1.set_ylabel(r'$\max (\varepsilon)$, $F_{sss}$')
ax2.set_ylabel(r'$\max (\varepsilon)$, $S_3$')
ax1.ticklabel_format(axis = "y", scilimits = (0, 0), useMathText = True)
ax2.ticklabel_format(axis = "y", scilimits = (0, 0), useMathText = True)
ax1.legend(handles = [p1, p2, p3, p4])
#plt.savefig('../../images/roterror-s3.png')
plt.show()
