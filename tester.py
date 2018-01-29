import numpy as np
from matplotlib import pyplot as plt
import lorenz
import nonlinear_drop
import interpolate
import ordinal_TSA as ot

uneven_intvl=0.02
even_intvl=0.01

arr = lorenz.get_lorenz(tmax=10000,n=1000000);
uneven_arr = nonlinear_drop.nonlinear_drop(arr=arr, lin_intvl=uneven_intvl);

uneven_time = uneven_arr[:,0];
uneven_series = uneven_arr[:,1];

even_time = arr[:,0];
even_series = arr[:,1];

print(uneven_time);

time1, even_series1 = interpolate.pick_nearest(uneven_time, uneven_series, sampling_rate=even_intvl);
time2, even_series2 = interpolate.average_nearest(uneven_time, uneven_series, sampling_rate=even_intvl);


plt.figure()
plt.plot(time2[:-1], even_series2[:-1], '.', label='linear');
plt.plot(time1[:-1], even_series1[:-1], '.', label='nearest');
plt.legend();
#plt.plot(uneven_time, uneven_series, '*', label='uneven')
#plt.plot(even_time, even_series, '-', label='original')
plt.savefig('series.png');

window = 1000
dim = 4

len0 = int(len(even_series) / window)
len1 = int(len(even_series1) / window)
len2 = int(len(even_series2) / window)

wpe0 = np.zeros(len0);
wpe_time0 = even_time[np.arange(0,len(even_series),window)[:-1]];

wpe1 = np.zeros(len1);
wpe_time1 = time1[np.arange(0,len(even_series1),window)[:-1]];

wpe2 = np.zeros(len2);
wpe_time2 = time2[np.arange(0,len(even_series2),window)[:-1]];

for i in range(len0):
  wpe0[i] = np.asarray(ot.permutation_entropy(even_series[i*window:(i+1)*window].reshape(-1,1),dim=4,step=1,w=1));

for i in range(len1):
  wpe1[i] = np.asarray(ot.permutation_entropy(even_series1[i*window:(i+1)*window].reshape(-1,1),dim=4,step=1,w=1));

for i in range(len2):
  wpe2[i] = np.asarray(ot.permutation_entropy(even_series2[i*window:(i+1)*window].reshape(-1,1),dim=4,step=1,w=1));

symb='.'
plt.figure();
#plt.plot(wpe_time0, wpe0, symb, label='original')
plt.plot(wpe_time1, wpe1, symb, label='nearest')
#plt.plot(wpe_time2, wpe2, symb, label='linear')
plt.legend();
#plt.show();
plt.savefig('wpe.png');

print(len(even_series))
print(len(even_series1))
print(len0);
print(len1);
print(len2);

