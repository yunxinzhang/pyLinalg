# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 11:56:37 2019

@author: zyx
"""

from LA.LU import lu
from LA.Matrix import Matrix

m = Matrix([[1,2],[3,4]])
a, b = lu(m)
print(a, b)
print(a.dot(b))