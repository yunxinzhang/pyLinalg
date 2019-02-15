# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 18:08:31 2019

@author: zyx
"""

from .Vector import Vector
from .Matrix import Matrix
from .GaussJordanElimination import rank

def GramSchmidtProcess(vecs):
    assert rank(Matrix(vecs)) == len(vecs) , "Not a full base"
    res = [vecs[0]]
    for r in range(1,len(vecs),1):
        p = vecs[r]
        for dr in range(len(res)):
            p = p - res[dr] * (res[dr].dot(p)/ res[dr].dot(res[dr]))
        res.append(p)
    return res

def QR(M):
    assert rank(M) == len(M), "Must a full rank Matrix."
    assert M.shape()[0] == M.shape()[1], "Not a square matrix."
    base = GramSchmidtProcess([M.get_col(i) for i in range(len(M))])
    Q = Matrix([base[i]/base[i].norm() for i in range(len(M))]).T()
    R = Q.T().dot(M)
    return Q, R
    
    