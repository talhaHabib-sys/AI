from sklearn import cluster,datasets
import matplotlib.pyplot as plt
import seaborn as sns

iriis=datasets.load_iris()
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

X=iriis.data[:20,:2]
y_iris=iriis.target

hc=AgglomerativeClustering(n_clusters=2,affinity='euclidean',linkage='ward')
y_hc=hc.fit_predict(X)
#plt.scatter(X[y_hc==0,0],X[y_hc==0,1],s=10,c='red',label='Cluster1')
#plt.scatter(X[y_hc==1,0],X[y_hc==1,1],s=10,c='blue',label='Cluster2')
#plt.show()
dendo=sch.dendrogram(sch.linkage(X,method='ward'))
plt.show()
