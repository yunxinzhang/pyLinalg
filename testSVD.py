# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 18:03:41 2019

@author: zyx
"""

import numpy as np
from scipy.linalg import svd 

M = np.array([[1,2,3],[4,5,6]])
u, s, vt = svd(M)