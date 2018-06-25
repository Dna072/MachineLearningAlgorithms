"""
    Using Adaboost algorithm to classify the terrain data
"""
from time import time
from tools.prep_terrain_data import makeTerrainData
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from tools.email_preprocess import preprocess
from visualize.class_vis import visualize_data

features_train, labels_train, features_test, labels_test = makeTerrainData()

#create classifier
clf = KNeighborsClassifier(n_neighbors=10, weights="distance")
t0 = time()
clf.fit(features_train, labels_train)
print "Training time: ", round(time() - t0, 3), "s"
#predict with model
t1 = time()
labels_pred = clf.predict(features_test)
print "Validation time: ", round(time()-t1), "s"

accuracy = accuracy_score(labels_test, labels_pred)
print "Accuracy: ", round(accuracy, 3)



