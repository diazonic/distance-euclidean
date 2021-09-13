import numpy as np
import matplotlib.pyplot as plt

#x = np.array([51, 62, 69, 64, 65, 52, 58, 57, 55])
#y = np.array([167, 182, 176, 173, 172, 174, 169, 173, 170])

x = np.array([51, 62, 69])
y = np.array([167, 182, 176])

demo = np.array([72,175])

plt.scatter(x,y)
plt.scatter(demo[0],demo[1],c='r',s=50)
plt.text(demo[0],demo[1],(demo[0],demo[1]))

for i in range(len(x)):
	plt.text(x[i],y[i],(x[i],y[i]))

res =[]
for i in range(len(x)):
	dist = np.sqrt(np.sum(np.square((x[i],y[i])-demo)))
	plt.plot((x[i],demo[0]),(y[i],demo[1]),c='k',linestyle=':')
	res.append(dist)
print(res)

from scipy.stats import rankdata

order = rankdata(res,method='ordinal')
print(order)

color = ['','r','g','b']
for i,j in enumerate(order):
	
	print(i)
	plt.text(x[i],y[i]+1,j,fontsize=20,c=color[j])


plt.show()
