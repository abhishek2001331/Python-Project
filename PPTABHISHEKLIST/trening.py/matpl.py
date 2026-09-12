import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 2, 3, 4, 5])
y = np.array([0, 1, 0, 1, 0])

x1 = np.array([2, 1, 5, 6, 8])
y1= np.array([0, 2, 0, 2, 0])

x2 = np.array([4, 5, 8, 6, 6])
y2= np.array([0, 3, 0, 3, 0])

x3 = np.array([7, 9, 4, 3, 1])
y3= np.array([0, 4, 0, 4, 0])

plt.subplot(2,2,1)
plt.plot(x1,y1,marker="*", linestyle="dashed" , color="blue", linewidth=2)
plt.title("My-Graph")
plt.grid()


plt.xlabel("x-Axis")
plt.ylabel("y-Axis")
# x1= np.array([])
# y1 = np.array([])
plt.subplot(2,2,2)
plt.plot(x,y,marker="*", linestyle="dashed" , color="blue", linewidth=2)

plt.subplot(2,2,3)
plt.plot(x2,y2,marker="*", linestyle="dashed" , color="blue", linewidth=2)

plt.subplot(2,2,4)
plt.plot(x3,y3,marker="*", linestyle="dashed" , color="blue", linewidth=2)
#plt.plot(x1,y1)
plt.show()