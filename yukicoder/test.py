import time
import random

A = [str(random.randint(0, 10000)) for i in range(50)]
S = ' '.join(A)
times = 10

print('method|elapsed[s]|type(A[0])')
print('---|---|---')
time_start_map = time.time()
for i in range(times):
    A = list(map(int, S.split()))
time_elapsed_map = time.time() - time_start_map
print('list(map)|', time_elapsed_map,'|',type(A[0]))

time_start_map = time.time()
for i in range(times):
    A = [map(int, S.split())]
time_elapsed_map = time.time() - time_start_map
print('[map]|', time_elapsed_map,'|',type(A[0]))


time_start_for = time.time()
for i in range(times):
    A = list(int(x) for x in S.split())
time_elapsed_for = time.time() - time_start_for
print('list(generator)|', time_elapsed_for,'|',type(A[0]))

time_start_for = time.time()
for i in range(times):
    A = [int(x) for x in S.split()]
time_elapsed_for = time.time() - time_start_for
print('[]|', time_elapsed_for,'|',type(A[0]))
