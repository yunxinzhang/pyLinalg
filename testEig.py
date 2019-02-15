# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 16:34:25 2019

@author: zyx
"""
import numpy as np
from numpy.linalg import eig

M = np.array([[1,2],[3,4]])
M = np.array([[1,0],[0,1]])
M = np.array([[1,2],[1,2]])

vals, vecs = eig(M)
