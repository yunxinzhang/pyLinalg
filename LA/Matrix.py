# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:22:39 2019

@author: zyx
"""

from .Vector import Vector

class Matrix():
    def __init__(self, list2d):
        self._val = [row[:] for row in list2d]
    def __repr__(self):
        return "Matrix({})".format(self._val)
    __str__ = __repr__
    
    def __getitem__(self, pos):
        r, c = pos
        return self._val[r][c]
    def shape(self):
        return (len(self._val), len(self._val[0]))
    def get_row(self, i):
        return Vector(self._val[i])
    def get_col(self, j):
        return Vector([self._val[i][j] for i in range(len(self._val))])
    
    def __len__(self):
        return len(self._val)
    def __add__(self, B):
        assert self.shape() == B.shape() , "Shape must match!"
        return Matrix([[a+b for a, b in zip(self.get_row(i), B.get_row(i))] \
                        for i in range(len(self._val))])
    
    def __sub__(self, B):
        assert self.shape() == B.shape() , "Shape must match!"
        return Matrix([[a-b for a, b in zip(self.get_row(i), B.get_row(i))] \
                        for i in range(len(self._val))])
    
    def __mul__(self, k):
        return Matrix([[a*k for a in self.get_row(i)] for i in range(len(self._val))])
    
    def __rmul__(self, k):
        return self * k
    
    def __truediv__(self , k):
        return (1/k)*self
    
    def __pos__(self):
        return self
    def __neg__(self):
        return -1*self
    @classmethod
    def zeros(cls, r, c):
        return cls([[0]*c for i in range(r)])
    
    def dot(self, B):
        if isinstance(B, Vector):
            assert self.shape()[1] == len(B), "Can't Mul"
            return Vector([self.get_row(i).dot(B) for i in range(self.shape()[0])])
        if isinstance(B, Matrix):
            assert self.shape()[1] == B.shape()[0], "Can't Mul"
            return Matrix([[self.get_row(i).dot(B.get_col(j)) for j in range(B.shape()[1])] \
                            for i in range(self.shape()[0])])
    
    def T(self):
        return Matrix([[e for e in self.get_col(i)] for i in range(self.shape()[1])])
    
    @classmethod
    def identity(cls, n):
        m = [[0]*n for _ in range(n)]
        for i in range(n):
            m[i][i] = 1
        return cls(m)
    
    