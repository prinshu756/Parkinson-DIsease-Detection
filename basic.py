import numpy as np
import matplotlib.pyplot as plt
import math 

x = np.random.random((8))
print(x.shape)
print(x)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.pie(x)
# plt.imshow(x)
plt.show()