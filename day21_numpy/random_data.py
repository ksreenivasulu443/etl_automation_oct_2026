import numpy as np


print("np.random.rand()", np.random.rand()) # float number between 0 to 1
print("np.random.randn()", np.random.rand(5)) # 5 float number between 0 to 1

print("np.random.randn()", np.random.rand(10,4))# 5 x 5 float number between 0 to 1

print("np.random.randint", np.random.randint(1,100)) #

print("np.random.randint", np.random.randint(18,100,5)) #

print("np.random.randint", np.random.randint(18,100,(10,1))) #


ls = ['silver', 'gold', 'platinum'] # tier

print("np.random.choice", np.random.choice(ls))