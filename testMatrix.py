# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:26:51 2019

@author: zyx
"""

from LA.Matrix import Matrix

A = Matrix([[1,2],[3,4]])
print(A)

print(A[0,1])
print("shape", A.shape() )

print("row", A.get_row(1))
print("col", A.get_col(0))
print("len", len(A))

B = Matrix([[2,4],[6,5]])
C = A + B
print("add", C)

D = A - B
print("sub", D)

E1 = A * 2
print("mul", E1)
E2 = 2 * A
print("rmul", E2)
F = A/2
print("div", F)
print("pos", +A)
print("neg", -A)
G = Matrix.zeros(4,5)
print(G)
H = A.dot(B)
print(H)
H2 = B.dot(A)
print(H2)
print("T", A.T())

I = Matrix.identity(5)
print(I)

