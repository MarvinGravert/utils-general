# from numpy.core.defchararray import center
from sklearn.datasets import make_blobs
# from matplotlib import pyplot as plt
# import pandas as pd
# import numpy as np
from typing import List,Dict,Tuple
# from sklearn.cluster import DBSCAN
# # Create test data: features (X) and labels (y)
seed:int=0
numFeatures:int=2
numSamples:int=200
centers:List[Tuple[float,float]]=[(1,1),(30,30)]
numCenters:int=len(centers)
# centers=3
# numCenters=centers

# points, labelCluster ,positionCenters= make_blobs(n_samples=numSamples, centers=centers, n_features=numFeatures,return_centers=True,random_state=seed)
# #X contains the (x,y) of each sample, y gives the membership of the 
# #concatenate matrix
# solutionMatrix:np.ndarray=np.hstack((points,labelCluster.reshape(numSamples,1)))
# #sort by label (==sort by last column)
# solutionMatrix:np.ndarray=solutionMatrix[solutionMatrix[:,-1].argsort()]
# # print(solutionMatrix)
# A1 = solutionMatrix[solutionMatrix[:, -1] == 1, :]
# # # # Group the data by labels
# # Xy = pd.DataFrame(dict(x1=points[:,0], x2=points[:,1], label=labelCluster))
# # groups = Xy.groupby('label')

# # # # Plot the blobs
# # fig, ax = plt.subplots()
# # colors = ["blue", "red", "green", "purple"]
# # for idx, classification in groups:
# #     classification.plot(ax=ax, kind='scatter', x='x1', y='x2', label=idx, color=colors[idx])
# # plt.show()
# model = DBSCAN(eps=0.30, min_samples=9)
# # fit model and predict clusters
# yhat = model.fit_predict(points)
# # retrieve unique clusters
# clusters = np.unique(yhat)
# # create scatter plot for samples from each cluster
# for cluster in clusters:
# 	# get row indexes for samples with this cluster
# 	row_ix = np.where(yhat == cluster)
# 	# create scatter of these samples
# 	plt.scatter(points[row_ix, 0], points[row_ix, 1])
# # show the plot
# plt.show()

# ##kmeans

# dbscan clustering
from numpy import unique
from numpy import where
from sklearn.datasets import make_classification
from sklearn.cluster import DBSCAN
from matplotlib import pyplot
# define dataset
X, _ = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=4)
X,*_=make_blobs(n_samples=numSamples, centers=centers, n_features=numFeatures,return_centers=True,random_state=seed)
# define the model
print(X)
model = DBSCAN(eps=0.30, min_samples=80)
# fit model and predict clusters
yhat = model.fit_predict(X)
# retrieve unique clusters
clusters = unique(yhat)
# create scatter plot for samples from each cluster
for cluster in clusters:
	# get row indexes for samples with this cluster
	row_ix = where(yhat == cluster)
	# create scatter of these samples
	pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
# show the plot
pyplot.show()