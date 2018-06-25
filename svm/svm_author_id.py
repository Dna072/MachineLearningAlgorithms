#!/usr/bin/python

import sys
import numpy as np
from time import time
from tools.email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

from visualize import class_vis
from tools.prep_terrain_data import makeTerrainData

sys.path.append("../tools/")

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels

features_train, features_test, labels_train, labels_test = preprocess()

#features_train, labels_train, features_test, labels_test = makeTerrainData()

# SVM C parameter testing
clf = SVC(kernel="rbf", C=10000)
t0 = time()
clf.fit(features_train, labels_train)
print "Training time: ", time() - t0, "s"
#class_vis.visualize_data(clf, features_test, labels_test, "features", "labels")
t1 = time()
labels_predict = clf.predict(features_test)
print "Predicting time: ", time() - t1, "s"
accuracy = accuracy_score(labels_test, labels_predict)

print "Accuracy: ", accuracy
print "Chris class items: ", np.count_nonzero(labels_predict == 1)
