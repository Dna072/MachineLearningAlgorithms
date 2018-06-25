#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

n_missing_total_payments = 0
n_email_addresses = 0
myList = [1, 3, 5, 7, 'a', 6]
print myList[1:]

for persons, features in enron_data.iteritems():

    if features["poi"]==True and type(features["total_payments"]) is str:
        n_missing_total_payments = n_missing_total_payments + 1
        print features

print persons
print "Missing total payments: ", n_missing_total_payments, "\nPercentage: ", (float(n_missing_total_payments)/float(len(enron_data)) * 100)