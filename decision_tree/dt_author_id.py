#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from tools.email_preprocess import preprocess
#from tools.prep_terrain_data import makeTerrainData
from sklearn import tree
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels

features_train, features_test, labels_train, labels_test = preprocess()

print "Number of features: ", len(features_train[0])
#decision tree
clf = tree.DecisionTreeClassifier(min_samples_split=40)
t0 = time()
clf.fit(features_train, labels_train)
print "Training time: ", round(time() - t0, 3), "s"
t1 = time()
labels_pred = clf.predict(features_test)
print "Predicting time: ", round(time() - t1, 3), "s"

accuracy = accuracy_score(labels_test, labels_pred)
print "Accuracy: ", round(accuracy, 3)