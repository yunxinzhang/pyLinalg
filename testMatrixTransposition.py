# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 10:44:45 2019

@author: zyx
"""

from matplotlib import pyplot as plt
from LA.Matrix import Matrix
import math

points = [[3, 4], [4, 6], [2, 5], [3, 4]]

x = [point[0] for point in points]
y = [point[1] for point in points]

plt.figure(figsize=(5,5))
plt.xlim(-8,8)
plt.ylim(-8,8)
plt.plot(x, y)


T = Matrix([[-1, 0], [0, 1]]) # y轴对称
T = Matrix([[1, 0], [0, -1]]) # x轴对称
T = Matrix([[-1, 0], [0, -1]])# 原点对称
theta = math.pi/3
T = Matrix([[math.cos(theta), math.sin(theta)], [-math.sin(theta), math.cos(theta)]]) # 旋转
T = Matrix([[2, 0], [0, 1.5]])# 缩放
T = Matrix([[1, 0.5], [0, 1]])# 错切
T = Matrix([[1, 0], [0.5, 1]])
P = Matrix(points)
R = T.dot(P.T())

x2 = [e for e in R.get_row(0)]
y2 = [e for e in R.get_row(1)]
plt.plot(x2, y2)
plt.show()