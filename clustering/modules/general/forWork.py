###GRPC init


# test()
###Generate DATA


#=>get x,y, label,center
###Apply kMeans

##=>
###send to server
#Prep data

#create stub

#receive Data 

#prepare for Checking

###Check data

##Plot Results
print(__doc__)

import numpy as np

from sklearn.cluster import DBSCAN,KMeans
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler


# #############################################################################
# Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
                            random_state=0)

# X = StandardScaler().fit_transform(X)
###############
#compute kmeans
k_means=KMeans(n_clusters=4, random_state=0).fit_predict(X)
k2_means=KMeans(n_clusters=4, random_state=0).fit_predict(X)
# print(k2_means)
# print(kMeans.cluster_centers_)

# # #############################################################################
# # Compute DBSCAN
db = DBSCAN(eps=0.3, min_samples=10).fit_predict(X)
print(db)
# core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
# core_samples_mask[db.core_sample_indices_] = True
# labels = db.labels_

# # Number of clusters in labels, ignoring noise if present.
# n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
# n_noise_ = list(labels).count(-1)

# # #############################################################################
# # Plot result
# import matplotlib.pyplot as plt
# plt.figure(1)
# plt.scatter(X[:, 0], X[:, 1], c=k_means)
# # # Black removed and is used for noise instead.
# plt.figure(2)
# unique_labels = set(labels)
# colors = [plt.cm.Spectral(each)
#           for each in np.linspace(0, 1, len(unique_labels))]
# for k, col in zip(unique_labels, colors):
#     if k == -1:
#         # Black used for noise.
#         col = [0, 0, 0, 1]

#     class_member_mask = (labels == k)

#     xy = X[class_member_mask & core_samples_mask]
#     plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
#              markeredgecolor='k', markersize=14)

#     xy = X[class_member_mask & ~core_samples_mask]
#     plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
#              markeredgecolor='k', markersize=6)

# plt.title('Estimated number of clusters: %d' % n_clusters_)
# plt.show()