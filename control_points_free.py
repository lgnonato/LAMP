from time import time
import numpy as np
from sklearn import datasets
from sklearn.manifold import MDS,TSNE
from scipy.stats.mstats import zscore
import matplotlib.pyplot as plt

from lamp import Lamp

iris = datasets.load_iris()
x = iris.data
y = iris.target


# including labels as the last column
data = np.hstack((x,y.reshape(y.shape[0],1)))


##### using Lamp
ts = time()
lamp_proj = Lamp(Xdata = data, label=True)
data_proj = lamp_proj.fit()
print('Took {}s'.format(time() - ts))

plt.scatter(data_proj[:,0],data_proj[:,1])
plt.scatter(data_proj[:,0],data_proj[:,1],c=data[:,-1])
plt.show()

