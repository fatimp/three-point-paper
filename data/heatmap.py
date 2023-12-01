#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

data = np.load('soil-s3.npy')

plt.figure(figsize = (8, 8), dpi = 300)
plt.rc('font', size = 20)
plt.imshow(np.where(data < 0.1, data, 0.1), extent = (0, 160*2.25, 160*2.25, 0))
plt.xlabel(r'$r_1 \cdot (1, 1, 0), \mu m$')
plt.ylabel(r'$r_2 \cdot (-1, 1, 0), \mu m$')
plt.savefig('../images/soil-s3.png')
