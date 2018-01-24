#!/usr/bin/python

import numpy as np
from matplotlib import pyplot as plt
import math
import lorenz

def nonlinear_drop(arr, lin_intvl=0.1):
    
  time = arr[:,0];
  data = arr[:,1];

  start = time[0];
  end = (math.log(time[-1]));

  uneven_spacing = np.exp(np.arange(start,end,lin_intvl));

  startidx = 0;
  newtime = [];
  newdata = [];

  for uneventime in uneven_spacing:
      while 1:
          if time[startidx] <= uneventime and time[startidx+1] > uneventime:
              newtime.append(time[startidx]);
              newdata.append(data[startidx]);
              break;
      
          startidx += 1;
  
  newtime = np.asarray(newtime).reshape(1,-1)
  newdata = np.asarray(newdata).reshape(1,-1);
  uneven_arr = np.concatenate((newtime, newdata), axis=0).T

  np.savetxt('uneven.txt', uneven_arr);
  np.savetxt('even.txt', arr);

  return uneven_arr; 
