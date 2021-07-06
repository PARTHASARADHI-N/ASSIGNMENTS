#3
import matplotlib as mpl
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
x=[1,2,3,4]
y1=[4,3,2,1]
y2=[10,20,30,40]
y3=[40,30,20,10]
y4=[1,2,1,2]
y5=[40,70,90,70]
plt.subplot(3,3,1)
plt.plot(x,y1)
plt.subplot(3,3,2)
plt.plot(x,y2)
plt.subplot(3,3,3)
plt.plot(x,y3)
plt.subplot(3,3,4)
plt.plot(x,y4)
plt.subplot(3,3,5)
plt.plot(x,y5)
plt.subplot(3,3,6)
plt.plot(y1,y2)
plt.subplot(3,3,7)
plt.plot(y2,y3)
plt.subplot(3,3,8)
plt.plot(y3,y4)
plt.subplot(3,3,9)
plt.plot(y4,y5)
plt.show()
