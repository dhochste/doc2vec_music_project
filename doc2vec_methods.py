"""
This file contains functions for loading Amazon Music Reviews dataframes
and performing Doc2Vec on the reviews.

Part of Project for Insight Data Science - Silicon Valley 2015a

David L. Hochstetler
1/20/15

Much thanks to Matt P. and Ben E. for the dataframe and Doc2Vec help!
"""


import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
import numexpr as ne 		# Used by pandas.query method
import sys
import re
import gensim, logging 		# For Doc2Vec
import cPickle as pickle 	# Used for pickling/unpickling files


def load_pickled_df(directory_path, file_path):
    """
    Load the df from pickled pandas dataframe
    """

    file_0 = directory_path+file_path

    with open(file_0, 'rb') as pickle_file:
        df = pickle.load(pickle_file)

    return df

def df_column_reduce(df):
	"""
	Keep only relevant columns. Using hard-coded column names from Amazon database
	"""
	df = df.drop(['product/price','review/helpfulness','review/score','review/profileName'], \
		axis=1, inPlace=False)

	df.columns = ['productId','title','summary','time','userId','tokenize']

	return df

def df_title_format(df):
	"""
	Replace spaces with underscores
	"""
	for i in range(len(df)):
		df['title'][i] = df['title'][i].replace(' ','_')

	return df

def df_review_collapse(df):
	"""
	Apply aggregation so there is only 1 row per review (append the tokenize column 
	for previous multiple lines of df for a single review)
	"""

	review_rows_list = []
	working_row = []

	for i,row in df.iterrows():
		if i == 0:
			working_row = row
		
		else:
			if row[0] == working_row[0]: # same review, add tokenized sentence
				working_row[-1].extend(row[-1])

			else: # new review
				review_rows_list.append(working_row)
				working_row = row

    review_rows_list.append(working_row) #add the last working_row compilation
    df_reviews = pd.DataFrame(review_rows_list, columns=df.columns)

	""" OLD STUFF - TOO SLOW!!!
	df = df.groupby(list(df.columns[:-1])).agg({'tokenize':'sum'})
	df.reset_index(inplace=True)
	"""
	return df_reviews

# In future, hope to have an 'artist' column and a 'genre' column in the dataframe
# For now, this function will just look up titles
def most_similar_titles(df, positive_terms=[], negative_terms=[], doc2Vec_model=None):
    all_search_terms = positive_terms +negative_terms
    
    # find the array of distances for all terms
    distances = doc2Vec_model.most_similar(positive=positive_terms, negative=negative_terms, topn=None)
    print distances[:5]
    #sort array and convert to indices rather than raw values
    best_distance_indices = argsort(distances)[::-1]
    print best_distances_indices[:5]
    title_scores = []
    for dist_index in best_distances_indices:
        vocab_word = doc2Vec_model.index2word[dist_index] # grab the word
        # if the word is a title that wasn'tin the search
        if vocab_word in df['titles'] and vocab_word not in all_search_terms:
            title_scores.append((vocab_word, float(distances[dist_index]))) # assign the score to the title
    return title_scores





