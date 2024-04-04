# ||||=====  Plot Math Functions  =====||||

# Sources:
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html
# https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot

from math import cos, pi, sin
from matplotlib import pyplot as plt
import numpy as np


# # ||||=====  Simple plot  =====||||
# plt.plot([1, 2, 3, 4])

# # ||||=====  Simple plot w/ two axis  =====||||
# x = np.arange(0, 5, 0.1)
# y = np.sin(x)
# plt.plot(x, y)

# # ||||=====  Simple plot w/ two axis and modified line shape and color  =====||||
# # Other color mods: r = red. g = green, b = blue; -- = dashed line, ^ = triangles, o = dots, s = square, etc...
# # ex. 'ro' = red dots, 'b--' = blue dashed line, 'g^' = green triangles.

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'b^')
# plt.axis([0, 6, 0, 20])

# # ||||=====  Evenly sampled time at 200ms intervals  =====||||

# t = np.arange(0., 5., 0.2)
# # Plotting three lines in one, one doubled and other tripled w/ red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', 
#          t, t**2, 'bs', 
#          t, t**3, 'g^')

# # ||||=====  IDK what is going on here but it looks cool  =====||||

# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
# plt.scatter('a', 'b', c='c', s='d', data=data)

# # ||||=====  Plotting three different graphs at once  =====||||
# # ||||=====   (Histogram, Line Graph, Dotted Graph)   =====||||

# names = ['group_a', 'group_b', 'group_c']
# values = [1, 10, 100]
# plt.figure(figsize=(9, 3))

# plt.subplot(131)
# plt.bar(names, values)

# plt.subplot(132)
# plt.scatter(names, values)

# plt.subplot(133)
# plt.plot(names, values)

# # ||||=====  Working with multiple figures and axes  =====||||

# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)

# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)

# plt.figure()
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')


# plt.xlabel('X')
# plt.ylabel('Y')
plt.suptitle('Graph')

plt.show()