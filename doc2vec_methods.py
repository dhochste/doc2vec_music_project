"""
This file contains functions for loading Amazon Music Reviews dataframes
and performing Doc2Vec on the reviews.

Part of Project for Insight Data Science - Silicon Valley 2015a

David L. Hochstetler
1/20/15

Much thanks to Matt P. and Ben E. for the dataframe and Doc2Vec help!
"""


import numpy as np
import matplotlib.pyplot as plt
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
		df['title'][i] = df_mini_gb['title'][i].replace(' ','_')

	return df

def df_review_collapse(df):
	"""
	Apply aggregation so there is only 1 row per review (append the tokenize column 
	for previous multiple lines of df for a single review)
	"""
	df = df.groupby(list(df.columns[:-1])).agg({'tokenize':'sum'})
	df.reset_index(inplace=True)

	return df





