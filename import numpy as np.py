import numpy as np

x = np.arange(-5,6,1)

y = 2 * x + 3

print("x is :",x)
print("y is :",y)

for i,j in zip(x,y):
    print(f"x = {i}, y = {j}")
    
