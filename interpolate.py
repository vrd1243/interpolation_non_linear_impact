#!/usr/bin/python

import numpy as np
from matplotlib import pyplot as plt

path = 'file.txt'

def average_nearest(time, data, sampling_rate=0.1, start_time=-1):
    
    span = time[-1] - time[0];
    samples = int(np.ceil(span/sampling_rate));

    even_series = np.zeros(samples);
    even_time = np.zeros(samples);

    nearest = 0;
    
    if start_time == -1 or start_time < time[0]:
        start_time = time[0];
    
    ts = start_time;
    for i in range(samples-1):
        while ts > time[nearest+1]:
            nearest += 1;
        
        even_time[i] = ts;
        if time[nearest+1] == time[nearest]:
            slope = 0
        else:
            slope =  (data[nearest+1] - data[nearest]) / (time[nearest+1] - time[nearest]);
        even_series[i] = slope * (ts - time[nearest]) + data[nearest];
        ts += sampling_rate;

    return even_time, even_series;


def pick_nearest(time, data, sampling_rate=0.1, start_time=-1):
    
    span = time[-1] - time[0];
    samples = int(np.ceil(span/sampling_rate));

    even_series = np.zeros(samples);
    even_time = np.zeros(samples);

    nearest = 0;

    if start_time == -1 or start_time < time[0]:
        start_time = time[0];
    
    ts = start_time;

    for i in range(samples-1):
        while ts > time[nearest+1]:
            nearest += 1;

        if nearest < len(time) - 1:
            if abs(ts - time[nearest]) > abs(ts - time[nearest+1]):
                even_series[i] = data[nearest+1];
            else:
                even_series[i] = data[nearest];

        even_time[i] = ts;
        ts += sampling_rate;

    return even_time, even_series;


def main():
    
    arr = np.loadtxt(path);
    time = arr[:,0];
    data = arr[:,1];
    time1, even_series1 = pick_nearest(time, data, sampling_rate);
    time2, even_series2 = average_nearest(time, data, sampling_rate);

    plt.figure();
    plt.plot(time1[:-1], even_series1[:-1],'.');
    plt.plot(time2[:-1], even_series2[:-1],'*');
    plt.savefig('plot.png');
    print(even_series2);
    print(time2);

