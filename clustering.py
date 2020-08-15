from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

pic = plt.imread('trees.png') 
print(pic.shape)
plt.imshow(pic)


pic_n = pic.reshape(pic.shape[0]*pic.shape[1], pic.shape[2])
pic_n.shape


kmeans = KMeans(n_clusters=64, random_state=0).fit(pic_n)
pic2show = kmeans.cluster_centers_[kmeans.labels_]


cluster_pic = pic2show.reshape(pic.shape[0], pic.shape[1], pic.shape[2])
plt.imshow(cluster_pic)
