# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 10:40:12 2019

@author: zyx
"""

from .Matrix import Matrix
from .Vector import Vector

def lu(M):
    assert M.shape()[0] == M.shape()[1], "简化版，必须是方阵"
    I = Matrix.identity(len(M))
    mat = [[e for e in M.get_row(i)] for i in range(len(M))]
    idm = [[e for e in I.get_row(i)] for i in range(len(I))]
    for r in range(len(mat)):
        if mat[r][r] == 0:
            return None, None
        for dr in range(r+1, len(mat), 1):
            coef = mat[dr][r] / mat[r][r]
            mat[dr] = [mat[dr][k] - coef * mat[r][k] for k in range(len(mat))]
            idm[dr] = [idm[dr][k] + coef * idm[r][k] for k in range(len(idm))]
    return Matrix(idm), Matrix(mat)