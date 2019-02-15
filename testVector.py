# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 10:34:13 2019

@author: zyx
"""

from LA.Vector import Vector

v = Vector([1,2,5])
print(v)
print(v[0])

v2 = Vector.zeros(5)
print("zeros", v2)
print("v2 len = ", len(v2))

v3 = Vector([3,4,5])
v4 = v + v3
print("add", v4)
v5 = v - v3
print("sub", v5)
print("norm({}) = ".format(v), v.norm())
v6 = v * 3
print(" * K >> " ,v6)
v7 = 4 * v
print("K *  >>",  v7)
v8 = v / 2
print(" / k >> ", v8)
print("positive >> ", +v)
print("negtive >>", -v)

v9 = v.normalize()
print("normalize >> " , v9)
try:
    v10 = v2.normalize()
    print("normalize >> " , v10)
except ZeroDivisionError:
    print("can't normalize")
