import numpy as np
from sklearn import datasets
from sklearn.manifold import MDS,TSNE
from scipy.stats.mstats import zscore
import matplotlib.pyplot as plt

from lamp import Lamp

######## Generating the Data #############

num_points = 500
x1 = np.random.multivariate_normal(np.zeros((20,)), 0.1*np.identity(20,dtype=float), num_points)
l = np.zeros((num_points,1))
x1 = np.hstack((x1,l))   # adding lable 0 as last column

x2 = np.random.multivariate_normal(np.ones((20,)), 0.1*np.identity(20,dtype=float), num_points)
l = np.ones((num_points,1))
x2 = np.hstack((x2,l))   # adding lable 1 as last column

x = np.vstack((x1,x2))
np.random.shuffle(x)

# randomly chosing the control points
sample_size = 15
samples = np.random.randint(0, high=num_points, size=(sample_size,))

######## Generating the Control Points #############

##### projecting control points with MDS #####
ctp_mds = MDS(n_components=2)
ctp_samples = ctp_mds.fit_transform(x[samples]-np.average(x[samples]))

# including ids of control points as the last column of the projected control points
ctp_samples = np.hstack((ctp_samples,samples.reshape(sample_size,1)))

######## Performing the projections in two stages #############

#####  Instantiating Lamp
lamp_proj = Lamp(Xdata = x[:num_points], control_points = ctp_samples, label=True)

#####  projecting first half of the data
data_proj = lamp_proj.fit()

plt.title('First Half')
plt.scatter(data_proj[:,0],data_proj[:,1],c=data_proj[:,-1])
plt.scatter(ctp_samples[:,0],ctp_samples[:,1],c='r',s=2)

#####  projecting second half of the data
data_proj = lamp_proj.fit(Xdata=x[num_points:])

plt.title('Second Half')
plt.scatter(data_proj[:,0],data_proj[:,1],marker='o',edgecolors='r',c=data_proj[:,-1])
plt.show()

