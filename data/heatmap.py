#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
import matplotlib as mpl

data = np.load('shale-avg.npy')

def fuck(x, pos):
    if pos%4 == 0:
        f = ticker.LogFormatterSciNotation(10, False)
        return f(x)
    else:
        return ''

plt.figure(figsize = (8, 8), dpi = 300)
plt.rc('font', size = 20)
plt.imshow(data, extent = (0, 160/2*2.25, 160/2*2.25, 0), norm = 'log')
cb = plt.colorbar()
cb.minorformatter = ticker.FuncFormatter(fuck)
plt.xlabel(r'$r_1\ [\mu m]$')
plt.ylabel(r'$r_2\ [\mu m]$')
plt.savefig('../images/shale-avg.png', bbox_inches = 'tight')
