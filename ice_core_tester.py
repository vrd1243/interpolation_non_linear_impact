import numpy as np
from matplotlib import pyplot as plt
import lorenz
import nonlinear_drop
import interpolate
import ordinal_TSA as ot
import pandas as pd

def interpolate_with_map(map_data, depth_data):
    
    age_series = [];
    depth_idx_series = [];
    map_depth = map_data[:,0];
    map_age = map_data[:,1];
    num_ele = len(map_depth);

    print(map_age);

    i = 1;

    for idx, d in enumerate(depth_data):
        if d < map_depth[i-1]:
            continue;
        
        while (i < num_ele - 1) and not (d <= map_depth[i] and d >= map_depth[i-1]):
            i += 1;
        
        if i == num_ele - 1:
            break; 

        slope = (map_age[i] - map_age[i-1]) / (map_depth[i] - map_depth[i-1]); 
        age_series.append(slope * (d - map_depth[i-1]) + map_age[i-1]);
        depth_idx_series.append(idx);
    
    return [np.asarray(depth_idx_series), np.asarray(age_series)];

# This will be our map.
map_data = np.loadtxt('age_vs_depth.txt', delimiter='\t');
map_depth = map_data[:,0];
map_age = map_data[:,1];

# Pull in the age data 
age_data = np.loadtxt('age.txt', delimiter=' ');
print(age_data[:,0], age_data[:,1]);

# Pull in the depth data 
depth_data = np.loadtxt('depth.txt', delimiter=' ');

mapped_series = interpolate_with_map(map_data, depth_data[:,0]);
mapped_idx = mapped_series[0];
mapped_age = mapped_series[1];

plt.figure();
plt.plot(depth_data[mapped_idx,0], mapped_series[1], '-');
plt.plot(map_depth, map_age, '-');
plt.savefig('mapping.png');

even_series = interpolate.average_nearest(mapped_age, depth_data[mapped_idx, 1], sampling_rate=1/20, start_time=-55.95);
print(even_series);
np.savetxt('ice_core_interpolation.txt', np.concatenate((even_series[0].reshape(-1,1), even_series[1].reshape(-1,1)), axis=1), fmt='%.3f');


samples=-1
slices=1000
plt.figure();
plt.plot(even_series[0][:samples:slices], even_series[1][:samples:slices],'*', label='Varad\'s interpolation');
plt.plot(age_data[:samples:slices,0], age_data[:samples:slices,1],'.', label='Tyler\'s interpolation');
plt.xlabel('Age in years');
plt.ylabel('dD (per mill)');
plt.legend();
plt.savefig('ice_core_interpolation.png');
