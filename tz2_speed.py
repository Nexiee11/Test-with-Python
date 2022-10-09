import timeit
import random
import matplotlib.pyplot as plt
from tz2f  import _max
import numpy
arr  = [random.sample(range(-1_000,1_000),k) for k in range(10,51)]

time_res = []
for x in arr:
    time_res += [timeit.timeit(lambda: _max(x))]

plot_data = [x for x in range(10,51)]

plt.plot(time_res,plot_data)
plt.title('Time to size for _max function',fontsize=25,color='red')
plt.xlabel('Time in seconds')
plt.ylabel('Size')
plt.show()
plt.yticks(10)

