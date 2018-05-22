import numpy as np
from sklearn import datasets
from sklearn.manifold import MDS,TSNE
from scipy.stats.mstats import zscore
import matplotlib.pyplot as plt

from lamp import Lamp

iris = datasets.load_iris()
x = iris.data
y = iris.target

# randomly chosing the control points
sample_size = 15
samples = np.random.randint(0, high=x.shape[0], size=(sample_size,))

##### projecting control points with MDS #####
ctp_mds = MDS(n_components=2)
ctp_samples = ctp_mds.fit_transform(x[samples]-np.average(x[samples]))

# including ids of control points as the last column of the projected control points
ctp_samples = np.hstack((ctp_samples,samples.reshape(sample_size,1)))

# including labels as the last column
data = np.hstack((x,y.reshape(y.shape[0],1)))

##### using Lamp
lamp_proj = Lamp(Xdata = data, control_points = ctp_samples, label=True)
data_proj = lamp_proj.fit()

plt.scatter(data_proj[:,0],data_proj[:,1],c=y)
plt.scatter(ctp_samples[:,0],ctp_samples[:,1],c='r',s=2)
plt.show()

