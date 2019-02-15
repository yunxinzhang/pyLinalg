# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:46:41 2019

@author: zyx
"""
from .Matrix import Matrix
from .Vector import Vector

class GaussJordanElimination():
    def __init__(self, M, b):
        if b == None:
            if isinstance(M, Matrix):
                self._Mb = [[e for e in M.get_row(i)] for i in range(len(M))]
            else:
                self._Mb = [[e for e in M[i]] for i in range(len(M))]
        elif isinstance(b, Vector):
            assert M.shape()[0] == len(b), "Rank must match."
            self._Mb = [[e for e in M.get_row(i)]+[b[i]] for i in range(len(b))]
        elif isinstance(b, Matrix):
            assert M.shape()[0] == b.shape()[0], "Rank must match."
            self._Mb = [[e for e in M.get_row(i)]+[e for e in b.get_row(i)] for i in range(len(b))]
        self._nrow = len(M)
        self._ncol = M.shape()[1]
        self._pvok = []
        self._cols = len(self._Mb[0])

    def eliminate(self):
        self._forward()
        self._backward()
        for i in range(len(self._pvok), self._nrow, 1):
            for j in range((self._ncol), (self._cols), 1):
                if abs(self._Mb[i][j]) > 1e-8:
                    return False
        return True
    
    def inv(self):
        assert len(self._Mb)*2 == len(self._Mb[0]), "Not A Square Matrix."
        self._forward()
        self._backward()
        return Matrix([[self._Mb[i][j] for j in range(self._ncol, self._cols, 1)] for i in range(self._nrow)])
    
    def _get_max_not_zero_item(self, r, c):
        maxitem, maxidx = self._Mb[r][c], r
        for i in range(r+1,  self._nrow, 1):
            if self._Mb[i][c] > maxitem:
                maxitem = self._Mb[i][c]
                maxidx = i
        if abs(maxitem) < 1e-8:
            return -1
        else:
            return maxidx
            
    def _forward(self):
        r, c = 0, 0
        for c in range(self._ncol):
            if abs(self._Mb[r][c]) < 1e-8:
                idx = self._get_max_not_zero_item(r, c)
                if(idx == -1):
                    continue
                else:
                    self._Mb[r], self._Mb[idx] = self._Mb[idx], self._Mb[r]
            self._Mb[r] = [ e / self._Mb[r][c] for e in self._Mb[r]]
            self._pvok.append(c)
            for i in range(r+1, self._nrow, 1):
                self._Mb[i] = [self._Mb[i][k] - self._Mb[r][k]*self._Mb[i][c] for k in range(self._cols)]
            r = r + 1
            
    def _backward(self):
        for ith in range(len(self._pvok)-1, -1, -1):
            for r in range(ith-1, -1, -1):
                self._Mb[r] = [self._Mb[r][k] - self._Mb[ith][k] * self._Mb[r][self._pvok[ith]] for k in range(self._cols) ]

def inv(M):
    assert len(M._val) == len(M._val[0]), "Must be a square matrix."
    gje = GaussJordanElimination(M, Matrix.identity(len(M._val)))
    return gje.inv()  

def rank(M):
    gje = GaussJordanElimination(M, None)
    gje.eliminate()
    return len(gje._pvok) 
        