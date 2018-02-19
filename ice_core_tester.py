import numpy as np
from matplotlib import pyplot as plt
import lorenz
import nonlinear_drop
import interpolate
import ordinal_TSA as ot
import pandas as pd

def interpolate_with_map(map_data, depth_series):
    
    age_series = [];
    map_age = map_data[:,0];
    map_depth = map_data[:,1];

    i = 1;

    for d in depth_series:
        if d <= map_depth[i] and d >= map_depth[i-1]:
            slope = (map_age[i] - map_age[i-1]) / (map_depth[i] - map_depth[i-1]); 
            age_series.append(slope * (d - map_depth[i-1]) + map_age[i-1]);
        else: 
            i += 1;
    
    return np.asarray(age_series);

# This will be our map.
map_data = np.loadtxt('age_vs_depth.txt', delimiter='\t');
map_depth = map_data[:,0];
map_age = map_data[:,1];

age_data = np.loadtxt('age.txt', delimiter=' ');
print(age_data);

# Pull in the depth data 
depth_data = np.loadtxt('depth.txt', delimiter=' ');
print(depth_data);

mapped_age = interpolate_with_map(map_data, depth_data[:,0]);

plt.figure();
plt.plot(depth_data[:,0], mapped_age, '-');
plt.plot(map_depth, map_age, '*');
plt.show();
plt.savefig('mapping.png');

