import numpy as np
import random
import time

x = random.randint(2, 7)
y = random.randint(2, 7)

array_1 = [[random.randint(1, 10) for _ in range(x)] for _ in range(y)]
array_2 = [[random.randint(1, 10) for _ in range(y)] for _ in range(x)]

matrices = (np.array(array_1), np.array(array_2))

start = time.perf_counter()
result = np.matmul(*matrices)
exec_time = time.perf_counter() - start

print('matrix A\n{}\n\nmatrix B\n{}'.format(*matrices))
print('\nA * B\n{}'.format(np.matmul(*matrices)))
print('\ncalculation time: {:0.4f} ms'.format(exec_time * 1000))

