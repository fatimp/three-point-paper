#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

data = np.load('shale-s3.npy')

plt.figure(figsize = (8, 8), dpi = 300)
plt.rc('font', size = 20)
plt.imshow(data, extent = (0, 160/2*2.25, 160/2*2.25, 0), norm = 'log')
plt.colorbar()
plt.xlabel(r'$r_1 \cdot (1, 1, 0), \mu m$')
plt.ylabel(r'$r_2 \cdot (-1, 1, 0), \mu m$')
plt.savefig('../images/shale-s3.png', bbox_inches = 'tight')
