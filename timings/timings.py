#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

legend = ['$S_3$', '$C_3$', '$F_{sss}$', '$F_{ssv}$', '$F_{svv}$']
names = map(lambda name: name + '.npy', ['s3', 'c3', 'surf3', 'surf2void', 'surfvoid2'])
colors = ['bo', 'rv', 'gP', 'k*', 'ms']

plt.figure(figsize = (10, 9), dpi = 300)
plt.rc('font', size = 24)

for (name, color) in zip(names, colors):
    data = np.load('gpu/' + name)
    plt.plot(data[:,0]**3, data[:,1], color + '-', linewidth = 3, markersize = 10)

plt.legend(legend)
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Number of voxels')
plt.ylabel('Time of execution [s]')
plt.savefig('timings-gpu.png')
