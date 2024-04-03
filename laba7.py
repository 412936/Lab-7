#Дружинина (6 вариант)
import numpy as np
import random
from time import perf_counter
import matplotlib.pyplot as plt


#Задание№1
list_1 = [random.random() for _ in range(1000000)]
list_2 = [random.random() for _ in range(1000000)]
np_array_1 = np.array(list_1)
np_array_2 = np.array(list_2)

start_time = perf_counter()
result = [list_1[i] * list_2[i] for i in range(len(list_1))]
end_time = perf_counter()
result_1 = end_time - start_time

start_time_np = perf_counter()
result_np = np.multiply(np_array_1, np_array_2)
end_time_np = perf_counter()
result_2 = end_time_np - start_time_np

print(f"Время выполнения операции поэлементного перемножения стандартных списков: {result_1} с")
print(f"Время выполнения операции поэлементного перемножения массивов NumPy: {result_2} с")
print(f"Разница: {result_1-result_2} с")

#Задание№2
data = np.genfromtxt('data2.csv', delimiter=',')
hist = np.array(data[:, 2])[1:]

plt.hist(hist, 30)
plt.title('Гистограмма')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.grid()
plt.show()

plt.hist(hist, 30, density=True)
plt.title('Нормализованная гистограмма')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.grid()
plt.show()

print(f'Cреднеквадратичное отклонение: {np.std(hist)}')


#Задание№3
x = np.linspace(-np.pi, np.pi, 100)
y = 1 / x
z = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z)
plt.title('3D  график')

plt.show()