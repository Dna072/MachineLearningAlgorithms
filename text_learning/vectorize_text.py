#!/usr/bin/python

import os
import pickle
import re
import sys

from tools.parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""

from_sara = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

# temp_counter is a way to speed up the development--there are
# thousands of emails from Sara and Chris, so running over all of them
# can take a long time
# temp_counter helps you only look at the first 200 emails in the list so you
# can iterate your modifications quicker

text_vocabulary = pickle.load(file("text_vocabulary.pkl"))
# for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
#     for path in from_person:
#         ### only look at first 200 emails when developing
#         ### once everything is working, remove this line to run over full dataset
#         path = os.path.join('..', path[:-1])
#         print path
#         email = open(path, "r")
#
#         ### use parseOutText to extract the text from the opened email
#         email_words = parseOutText(email)
#         ### use str.replace() to remove any instances of the words
#         ### ["sara", "shackleton", "chris", "germani"]
#         signature_words = ["sara", "shackleton", "chris", "germani"]
#         for word in signature_words:
#             email_words = email_words.replace(word, "")
#         ### append the text to word_data
#         word_data.append(email_words)
#         ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
#
#         if from_person.name == "from_sara.txt":
#             from_data.append(0)
#         elif from_person.name == "from_chris.txt":
#             from_data.append(1)
#
#         email.close()
#
# print "emails processed"
# from_sara.close()
# from_chris.close()
#
# pickle.dump(word_data, open("your_word_data.pkl", "w"))
# pickle.dump(from_data, open("your_email_authors.pkl", "w"))
#
# print word_data[152]
#
# # in Part 4, do TfIdf vectorization here
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
#
# vectorizer = TfidfVectorizer(stop_words=ENGLISH_STOP_WORDS)
# tfidf_matrix = vectorizer.fit_transform(word_data)
# text_vocabulary = vectorizer.get_feature_names()
#
# pickle.dump(text_vocabulary, open("text_vocabulary.pkl", "w"))


print "No. of words: ", len(text_vocabulary)
print "text_vocab[0]: ", text_vocabulary[0]