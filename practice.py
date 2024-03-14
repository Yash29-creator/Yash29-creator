# practice sheet
print("hello boss")
import numpy as np
import time
SIZE= 1000000
l1=range(SIZE)
l2=range(SIZE)
a1=np.arange(SIZE)
a2=np.arange(SIZE)
#list time
start = time.time()
result= [ (x+y) for x,y in zip(l1,l2)]
print("Time taken by Python List is", (time.time()-start)*1000)
#numpy array time
start = time.time()
result = a1+a2
print("Time taken by Numpy array is", (time.time()-start)*1000)