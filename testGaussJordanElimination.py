# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:57:59 2019

@author: zyx
"""

from LA.GaussJordanElimination import GaussJordanElimination
from LA.GaussJordanElimination import inv, rank
from LA.Matrix import Matrix
from LA.Vector import Vector

M = Matrix([[1,2], [3,4]])
b = Vector([3, 7])
elm = GaussJordanElimination(M, Matrix([[1,0],[0,1]]))
print("inv >> ", elm.inv())
print("Inv >> ", inv(M))
print("Rank >> ", rank(M))
M = Matrix([[1,2,3], [2,4,5]])
b = Vector([3, 7])
M = Matrix([[1,2,-2], [2,-3,1], [3, -1, 3]])
b = Vector([6, -10, -16])
M = Matrix([[1,-1, 2, 0, 3], [-1, 1, 0, 2, -5], [1, -1, 4, 2, 4], [-2, 2, -5, -1, -3]])
b = Vector([1, 5, 13, -1])
M = Matrix([[1,2], [2,4]])
print("Rank >> ", rank(M))
b = Vector([3, 7])

elm = GaussJordanElimination(M,b)
print(elm._Mb) 
M._val[0][0] = 99
print(M._val)
print(elm._Mb)

print("True >> ", elm.eliminate())
print(elm._Mb )
print(elm._pvok)
