import numpy as np
import time

n = 1_000_000
data = list(range(n))

arr = np.arange(n)

start = time.time()
total_list = 0
for x in data:
    total_list += x
print("Список (цикл):", time.time() - start, "сек")

start = time.time()
total_np = arr.sum()
print("NumPy (sum):  ", time.time() - start, "сек")

print("Результаты равны?", total_list == total_np)

# if __name__ == "__speed_test__":
