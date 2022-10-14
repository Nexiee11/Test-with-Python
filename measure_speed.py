import timeit
import random
import matplotlib.pyplot as plt
import f12
import numpy 
test_arr = [1,10,20,30,50,100]
arr = [random.sample(range(-1_000,1_000),k) for k in test_arr]

time_res = {x: ''  for x in test_arr}
for x in arr:
    time_res[len(x)] = timeit.timeit(lambda:f12.all_func(x))

for x in time_res: 
    print(f'Result for {x} numbers is {time_res.get(x)}')
