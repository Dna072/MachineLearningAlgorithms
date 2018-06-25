#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from tools.email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score



### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()



classifier = GaussianNB()
t0 = time()
classifier.fit(features_train, labels_train)

#get training time
training_time = time() - t0

t1 = time()
labels_predict = classifier.predict(features_test)
prediction_time = time() - t1
accuracy = accuracy_score(labels_test, labels_predict)

print 'training_time: ', round(training_time, 3), 's'
print 'prediction_time: ', round(prediction_time, 3), 's'
print 'accuracy: ', accuracy
#########################################################


