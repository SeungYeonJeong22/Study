import numpy as np
import matplotlib.pyplot as plt
import random

#seed로 난수값 고정
random.seed(123)
"""---------1차원---------
x = random.sample(range(1,101),50)
print('>>>>x ',x)
y = [0 for val in x]
print('>>>>y ',y)

fig, ax = plt.subplots()
fig.set_size_inches(12,1)
for grid_pt in [20,40,60,80]:
    plt.axvline(x = grid_pt,color = 'silver')
plt.xlabel('Dim #1')
plt.scatter(x,y)
plt.show()
"""

"""---------2차원---------
x = random.sample(range(1,101),50)
y = random.sample(range(1,101),50)

print('>>>>x ',x)
print('>>>>y ',y)

n = list(range(1,51))

fig, ax = plt.subplots()
fig.set_size_inches(6,6)
# for i,txt in enumerate(n):
#     plt.annotate(txt,(x[i],y[i]))
ax.set_xlabel('Dim #1',fontsize = 15)
ax.set_ylabel('Dim #2',fontsize = 15)
plt.scatter(x,y)
plt.show()
"""

"""---------3차원---------
from mpl_toolkits import mplot3d
x = random.sample(range(1,101),50)
y = random.sample(range(1,101),50)
z = random.sample(range(1,101),50)

print('>>>>x ',x)
print('>>>>y ',y)
print('>>>>z ',y)

fig = plt.figure()
ax = fig.add_subplot(1,1,1,projection = '3d')

fig.set_size_inches(6,6)
ax.scatter(x,y,z)

ax.set_xlabel('Dim #1',fontsize = 15)
ax.set_ylabel('Dim #2',fontsize = 15)
ax.set_zlabel('Dim #3',fontsize = 15)
plt.show()
"""