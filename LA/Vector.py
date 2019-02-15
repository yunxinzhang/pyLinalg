# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 10:26:57 2019

@author: zyx
"""
import math

class Vector():
    # 构造函数
    def __init__(self, lst):
        self._val = lst
    # cmd arr
    def __repr__(self):
        return "Vector({})".format(", ".join([str(e) for e in self._val]))
    # print(arr)
    def __str__(self):
        return "({})".format(", ".join([str(e) for e in self._val]))
    # arr[0]
    def __getitem__(self, i):
        return self._val[i]
    # len
    def __len__(self):
        return len(self._val)
    # zeros
    @classmethod
    def zeros(cls, n):
        return cls([0]*n)
    
    # +
    def __add__(self, v):
        assert len(self) == len(v), "Length must match!"
        return Vector([a+b for a, b in zip(self, v)])
                
    # -
    def __sub__(self, v):
        assert len(self) == len(v), "Length must match!"
        return Vector([a-b for a, b in zip(self, v)]) 
    # k
    def __mul__(self, k):
        return Vector([e * k for e in self]) 
    # k
    def __rmul__(self, k):
        return Vector([e * k for e in self]) 
    def __truediv__(self, k):
        return (1/k)*self
    # def positive, negtive
    def __pos__(self):
        return self
    def __neg__(self):
        return -1 * self
    
    # norm
    def norm(self):
        return math.sqrt(sum([e**2 for e in self._val]))
    # normalize
    def normalize(self):
        if self.norm() < 1e-8:
            raise ZeroDivisionError("Divide Zero.")
        return 1/self.norm()*self
    # dot
    def dot(self, u):
        assert len(self) == len(u), "Length must match!"
        return sum([a*b for a,b in zip(self, u)])