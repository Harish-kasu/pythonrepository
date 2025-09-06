from numpy import *

arr = array([1,2,3,4,5,6,7], dtype=float)

a = linspace(1, 20, 4 , dtype = float)
b = logspace(1, 20, 4 , dtype = float)
print(a)
print(b)
m1 = matrix([[1,2,3],[4,5,6],[7,8,9]])
m2 = matrix([[1,2,3],[4,5,7],[6,8,9]])
m3 = m1 + m2
m4 = m1 * m2
print(m3, m4) 

