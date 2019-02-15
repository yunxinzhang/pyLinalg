# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 18:28:23 2019

@author: zyx
"""

from LA.Vector import Vector
from LA.Matrix import Matrix
from LA.GramSchmidtProcess import GramSchmidtProcess, QR

base = [Vector([1,2]), Vector([3,4])]
base = [Vector([1,0]), Vector([0,4])]
res = GramSchmidtProcess(base)
print(res)

M = Matrix([[1,2],[3,4]])
Q, R = QR(M)
print(Q)
print(R)
print(Q.dot(R))