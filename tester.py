import numpy as np
from matplotlib import pyplot as plt
import lorenz
import nonlinear_drop
import interpolate

arr = lorenz.get_lorenz();
uneven_arr = nonlinear_drop.nonlinear_drop(arr=arr, lin_intvl=0.2);


print(arr);
print(uneven_arr);

uneven_time = uneven_arr[:,0];
uneven_data = uneven_arr[:,1];

even_time = arr[:,0];
even_data = arr[:,1];

time1, even_series1 = interpolate.pick_nearest(uneven_time, uneven_data, sampling_rate=0.01);
time2, even_series2 = interpolate.average_nearest(uneven_time, uneven_data, sampling_rate=0.01);

print(time2)
print(even_series2);

plt.figure()
plt.plot(time2[:-1], even_series2[:-1], '.');
plt.plot(uneven_time, uneven_data, '*')
plt.plot(even_time, even_data, '-')

plt.savefig('plot.png')

