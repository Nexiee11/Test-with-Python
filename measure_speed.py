import timeit
import random
import matplotlib.pyplot as plt
from tz2f  import _max,_min,_mult,_sum
import numpy
arr  = [random.sample(range(-1_000,1_000),k) for k in range(10,51)]

time_res_max,time_res_mult,time_res_sum,time_res_min = [],[],[],[] 
for x in arr:
    time_res_max += [timeit.timeit(lambda: _max(x))] 
    time_res_min += [timeit.timeit(lambda: _min(x))]
    time_res_sum += [timeit.timeit(lambda: _sum(x))]
    time_res_mult += [timeit.timeit(lambda: _mult(x))] 

print(len(time_res_max),len(time_res_min))
