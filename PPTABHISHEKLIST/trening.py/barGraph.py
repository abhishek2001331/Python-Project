import matplotlib.pyplot as plt
x = ['s1','s2','s3']
y = [91 , 90 ,87]
plt.subplot(2,2,2)
plt.bar(x,y, color='black' ,width=0.4)


plt.subplot(2,2,1)
plt.plot(x,y, color='black')
plt.show()