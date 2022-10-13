import timeit
import random
import matplotlib.pyplot as plt
import f12
import numpy
arr = [random.sample(range(-1_000,1_000),k) for k in [1,10,20,30]]

time_res = {x: ''  for x in [1,10,20,30]}
for x in arr:
    time_res[len(x)] = timeit.timeit(lambda:f12.all_func(x))

for x in time_res: 
    print(f'Result for {x} numbers is {time_res.get(x)}')
