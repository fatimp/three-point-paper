#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

data = np.load('shale-s3.npy')

plt.figure(figsize = (8, 8), dpi = 300)
plt.rc('font', size = 20)
plt.imshow(np.where(data < 0.1, data, 0.1), extent = (0, 160*2.25, 160*2.25, 0))
plt.xlabel(r'$x, \mu m$')
plt.ylabel(r'$y, \mu m$')
plt.savefig('../images/shale-s3.png')
